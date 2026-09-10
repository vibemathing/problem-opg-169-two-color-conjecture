#!/usr/bin/env python3
"""Decode, byte-check, and replay the S06 Cycle 4 source capsule.

Candidate-only. The contained cross-checking implementations share the original
generator trust domain; successful execution is not independent verification.
"""
from __future__ import annotations
import base64, hashlib, io, json, lzma, os, subprocess, sys, tarfile, tempfile
from pathlib import Path

CAPSULE = "opg169-a01-s06-c05-cycle4-source-capsule.json"
EXPECTED_FORMAT = "opg169-s06-c05-cycle4-multipart-source-capsule-v1"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    here = Path(__file__).resolve().parent
    cap_bytes = (here / CAPSULE).read_bytes()
    cap = json.loads(cap_bytes.decode("utf-8"))
    if cap.get("format") != EXPECTED_FORMAT or cap.get("verdict") != "candidate_only":
        fail("unexpected capsule identity")

    parts = sorted(cap["parts"], key=lambda row: row["index"])
    if len(parts) != cap["part_count"] or [row["index"] for row in parts] != list(range(len(parts))):
        fail("capsule part index mismatch")
    chunks = []
    for row in parts:
        part = (here / row["path"]).read_bytes()
        if len(part) != row["bytes"] or digest(part) != row["sha256"]:
            fail(f"capsule part mismatch: {row['path']}")
        chunks.append(part)
    b64 = b"".join(chunks)
    if len(b64) != cap["base64_bytes"] or digest(b64) != cap["base64_sha256"]:
        fail("base64 payload mismatch")
    compressed = base64.b64decode(b64, validate=True)
    if len(compressed) != cap["compressed_bytes"] or digest(compressed) != cap["compressed_sha256"]:
        fail("compressed payload mismatch")
    raw = lzma.decompress(compressed)
    if len(raw) != cap["decoded_tar_bytes"] or digest(raw) != cap["decoded_tar_sha256"]:
        fail("decoded tar mismatch")

    expected = {row["path"]: row for row in cap["files"]}
    with tempfile.TemporaryDirectory(prefix="opg169-s06-c05-") as td:
        root = Path(td)
        seen = set()
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as tf:
            for member in tf.getmembers():
                name = member.name
                if member.isdir():
                    continue
                if not member.isfile() or name.startswith("/") or ".." in Path(name).parts or "/" in name:
                    fail(f"unsafe capsule member: {name!r}")
                if name not in expected or name in seen:
                    fail(f"unexpected or duplicate member: {name}")
                src = tf.extractfile(member)
                if src is None:
                    fail(f"unreadable member: {name}")
                data = src.read()
                row = expected[name]
                if len(data) != row["bytes"] or digest(data) != row["sha256"]:
                    fail(f"member mismatch: {name}")
                (root / name).write_bytes(data)
                seen.add(name)
        if seen != set(expected):
            fail("capsule member set mismatch")

        proc = subprocess.run(
            [sys.executable, str(root / "s06-cycle4-replay.py")],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=300,
            check=False,
            env={**os.environ, "PYTHONHASHSEED": "0"},
        )
        if proc.returncode != 0:
            sys.stderr.buffer.write(proc.stderr)
            fail(f"contained replay failed with exit {proc.returncode}")
        try:
            result = json.loads(proc.stdout.decode("utf-8"))
        except Exception as exc:
            fail(f"contained replay did not emit JSON: {exc}")
        if result.get("status") != "ok" or result.get("verdict") != "candidate_only" or result.get("root_closed") is not False:
            fail("contained replay returned an unexpected status")
        got = {
            "c37_catalogue_sha256": result["outputs"]["c37_catalogue"]["sha256"],
            "c37_original_sha256": result["outputs"]["c37_original_replay"]["sha256"],
            "c39_inherited_sha256": result["outputs"]["c39_inherited"]["sha256"],
            "summary_sha256": result["outputs"]["postprocess"]["sha256"],
            "audit_sha256": result["outputs"]["dual_oracle_audit"]["sha256"],
        }
        if got != cap["expected_outputs"]:
            fail("regenerated output digest set mismatch")
        print(json.dumps({
            "status":"ok",
            "verdict":"candidate_only",
            "capsule_sha256":digest(cap_bytes),
            "source_files":len(expected),
            "source_parts":len(parts),
            "decoded_tar_sha256":cap["decoded_tar_sha256"],
            "regenerated_outputs":got,
            "contained_replay":result,
            "trust_boundary":"same-generator reproducibility check; not an independent verifier receipt",
        }, sort_keys=True, separators=(",",":")))


if __name__ == "__main__":
    main()

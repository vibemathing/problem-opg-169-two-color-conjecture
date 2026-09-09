#!/usr/bin/env python3
"""Decode and verify losslessly transported S16 artifacts; candidate-only."""
from __future__ import annotations
import argparse, base64, hashlib, pathlib, zlib

SPECS = {
    "opg169-s16-cycle3-substantive-glue-kernel.lean.zlib.b64": ("opg169-s16-cycle3-substantive-glue-kernel.lean", 25669, "24957608b453a102e70ad87465c3780b75861de697fcb121b0e7ddf78e72fc14"),
    "opg169-s16-cycle4-d19-ledger.json.zlib.b64": ("opg169-s16-cycle4-d19-ledger.json", 12948, "d53e445880e7b934d0724fe45737ea05a4e0e6b69e9d29e2a3514d6dd860207f"),
    "opg169-s16-cycle4-formalization-receipt.json.zlib.b64": ("opg169-s16-cycle4-formalization-receipt.json", 9713, "0d15c8801dd096d80ba3c134e8998105e935ea37c101097624738b2d164864f7"),
    "opg169-s16-cycle4-normalized-root-cut.lean.zlib.b64": ("opg169-s16-cycle4-normalized-root-cut.lean", 45698, "9b7e4d87b6efc4e18c7ef83b3e08e28e44a43b13ed53585a24f2a09523d60016"),
    "opg169-s16-cycle4-proof-map.md.zlib.b64": ("opg169-s16-cycle4-proof-map.md", 9948, "3c47586dbf43b41e6ee041e8b35078fd11ac4fee91efaab79af82080f0fe8b4b"),
    "opg169-s16-cycle4-static-audit.py.zlib.b64": ("opg169-s16-cycle4-static-audit.py", 6472, "afecc691ab0a220fe21811b075e938550252dffc103653b4011ea5d2b4c07b30"),
}

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent)
    ap.add_argument("--output-dir", type=pathlib.Path, required=True)
    args = ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for encoded_name, (decoded_name, expected_size, expected_sha) in SPECS.items():
        encoded = (args.source_dir / encoded_name).read_text(encoding="ascii")
        data = zlib.decompress(base64.b64decode(encoded))
        actual_sha = hashlib.sha256(data).hexdigest()
        if len(data) != expected_size or actual_sha != expected_sha:
            raise SystemExit(f"integrity failure: {encoded_name}")
        (args.output_dir / decoded_name).write_bytes(data)
        print(f"ok {decoded_name} {len(data)} {actual_sha}")

if __name__ == "__main__":
    main()

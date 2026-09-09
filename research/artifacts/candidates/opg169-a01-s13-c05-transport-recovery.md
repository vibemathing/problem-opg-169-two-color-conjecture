# S13 Cycle 5 — transport recovery

```text
verdict: candidate_only
base_revision: dc6ee891ed7614602e88d48a57314416082dd022
branch: web/attempt-opg169-a01-s13-c05-transport-recovery-20260910
recovered_payload: exact S13 Cycle 4 bundle
new_mathematical_claims: false
L_join: NOT_CERTIFIED
root_closed: false
```

Cycle 4 existed only as local user-facing files. This recovery transaction preserves the exact 44,349-byte ZIP as four UTF-8 base64 chunks, an immutable manifest, and a bounded unpack/audit program.

## Recovered package

- ZIP SHA-256: `407358260e8b690af86c20b951543e9ce8dc6eaee55d545b6b6619577f19d9eb`
- ZIP members: **15**
- Text chunks: **4**
- CRC, member-set, byte-size, member SHA-256, and inner digest-manifest checks: **pass**
- Source-to-reassembled member comparisons: **all byte-equal**

The binary ZIP itself is not committed because this channel's repository writer accepts UTF-8 text. Running the unpacker reconstructs all fifteen original Cycle 4 files exactly.

## Preserved mathematical ceiling

No theorem, selector, witness, charge computation, or gap order is altered. The recovered package continues to state that the mission-supplied universal D/19 rule is an opaque candidate without proof/certificate payload; conditional on that import, the exact local frontier is C37 D/3. The global negative-face-to-parent generation theorem remains absent.

The unpack audit checks transport bytes only. It is not an independent mathematical verifier and cannot create Evidence, Result, or root closure.

## Replay

```bash
python3 opg169-a01-s13-c05-cycle4-unpack.py \
  opg169-a01-s13-c05-cycle4-capsule-manifest.json \
  --root . \
  --extract recovered-cycle4 \
  --output opg169-a01-s13-c05-cycle4-unpack-output.json
```

After extraction, `recovered-cycle4/r08_s13_cycle4_commands.txt` contains the original Cycle 4 replay commands.

```text
best_verified_result: none
root_closed: false
```

# S10 Cycle 4 — S13-C B46 source binding note

`candidate_only`; no mathematical row verdict is produced.

Fresh protected main at the audit cutoff is
`8541c137f7769ec29c1f6043f017b8cace9efc87`.

The mission requests 46 exact S13-C Bcrit rows. Fresh repository search finds
no identity-bound S13-C `4300/B46` artifact or packet. The merged S01 Cycle-6
candidate separately records that same source gate as open.

The only plausible historical carrier is open PR #54 at
`e68936730ed8b28469b568d4958cf569cd1ac078`. Its manifest names the expected
registry/source-state member digests, but its committed text capsule is not
self-consistent with its own unpacker:

- manifest: `chars_without_newline=14783` for part01;
- actual Git blob `1ebfc1ba59f4ca7f099b23990d123e0cb642b8b5`: 14,783 raw
  bytes and ends with newline;
- unpacker: `raw.decode('ascii').strip()` before comparing the length;
- therefore stripped length is at most 14,782, so the manifest assertion cannot
  pass.

The current PR #54 head also has a failed candidate-gate run
`34417596395` (`web-pr-diff-boundary` and `web-attempt-packet` failed).

S10 does not use PR #54's producer checker/consumer/report to reverse-engineer
the missing rows. That would break the clean-room boundary and would not repair
the source identity.

Required repair: publish exact plain registry/source-state bytes matching the
frozen member digests, or publish a new capsule transaction that reconstructs
the advertised ZIP/member digests and passes candidate gates. Then rerun S10
from the data specification.

Disposition:
`S13C_B46_SOURCE_BINDING=NOT_VERIFIABLE_CORRUPT_TRANSPORT`;
46 expected mission slots, 0 source row IDs recovered, 0 consumed, 46 blocked.
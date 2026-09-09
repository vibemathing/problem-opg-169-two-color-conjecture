"""Bounded exact certificate unpacking; no code execution or admission."""
import base64
import hashlib
import json
import lzma
from pathlib import Path

D = Path('research/artifacts/candidates')
ARCHIVE = D/'opg169-a01-c36-incoming-certificate-archive.json'
DEST = D/'opg169-a01-c36-incoming-certificate.json'
EXPECTED = 'd8c9873256df0dde3c09ebbf5fb2a794b52bf83c2ab601bbf6791f01ba0f08d3'


def main():
    raw = ARCHIVE.read_bytes()
    if len(raw) > 65536:
        raise ValueError('archive size limit')
    obj = json.loads(raw)
    if obj['decoded_sha256'] != EXPECTED or obj['decoded_bytes'] != 58403:
        raise ValueError('frozen certificate identity')
    packed = base64.b64decode(obj['data'], validate=True)
    decoder = lzma.LZMADecompressor(memlimit=134217728)
    content = decoder.decompress(packed, max_length=58404)
    if not decoder.eof or decoder.unused_data or len(content) != 58403:
        raise ValueError('bounded decode or trailing data')
    if hashlib.sha256(content).hexdigest() != EXPECTED:
        raise ValueError('decoded digest')
    json.loads(content)
    if DEST.exists() and DEST.read_bytes() != content:
        raise ValueError('refuse to overwrite different certificate')
    DEST.write_bytes(content)
    print(json.dumps({'verdict':'candidate_only','decoded_bytes':len(content),'decoded_sha256':EXPECTED,'status':'assembled'}))

if __name__ == '__main__':
    main()

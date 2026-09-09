#!/usr/bin/env python3
"""One-command candidate replay for the S08 Cycle 4 recovery capsule."""
from __future__ import annotations
import base64, concurrent.futures, hashlib, io, json, pathlib, subprocess, sys, tarfile, tempfile

D=pathlib.Path(__file__).resolve().parent
PYTHON=sys.executable
MANIFEST=D/'opg169-s08-cycle4-capsule-manifest.json'
SMALL={
 'pc':D/'opg169-s08-cycle4-plane-check.py',
 'po':D/'opg169-s08-cycle4-plane-output.json',
 'fc':D/'opg169-s08-cycle4-anchor-check.py',
 'fo':D/'opg169-s08-cycle4-anchor-output.json',
}
EXPECTED={
 'ur':'e0161a3680e5626412b7a83bc99f0563407090f22744d5cde9b6b60e61103127',
 'ar':'5ac55ef87c52dbfc16c88096dbb06c8d4fe237d1e84dd4261fc48739e97653dd',
 'po':'d8bb3cc4821dd78bea1abfe289e6123562fdd69fa2a9207cf980e139efaa6fb2',
 'fo':'aafc9415d3a6e264240eb7f8ff3f0500157fd15b0d3fa8b2d61bbaf9bfba9e54',
}

def digest_bytes(x:bytes)->str:return hashlib.sha256(x).hexdigest()
def digest(p:pathlib.Path)->str:return digest_bytes(p.read_bytes())
def run(args:list[str],timeout:int=180)->dict:
    r=subprocess.run(args,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
    if r.returncode:
        raise RuntimeError({'args':args,'returncode':r.returncode,'stderr':r.stderr[-2000:]})
    return json.loads(r.stdout)

def reconstruct(root:pathlib.Path)->dict[str,pathlib.Path]:
    m=json.loads(MANIFEST.read_text(encoding='utf-8'))
    assert m['format']=='opg169-s08-cycle4-large-capsule-v1'
    pieces=[]
    for row in m['chunks']:
        p=D/pathlib.Path(row['path']).name
        b=p.read_bytes();assert len(b)==row['bytes'];assert digest_bytes(b)==row['sha256']
        pieces.append(b)
    raw=base64.b64decode(b''.join(pieces),validate=True)
    assert len(raw)==m['archive_bytes'];assert digest_bytes(raw)==m['archive_sha256']
    expected={row['path']:row for row in m['members']}
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
        names=tf.getnames();assert set(names)==set(expected)
        for name in names:
            pp=pathlib.PurePosixPath(name)
            assert not pp.is_absolute() and '..' not in pp.parts
            data=tf.extractfile(name).read()
            row=expected[name];assert len(data)==row['bytes'];assert digest_bytes(data)==row['sha256']
            dst=root/pp;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data)
    c=root/'research/artifacts/candidates'
    return {
      'ug':c/'opg169-s08-cycle4-universal-generate.py',
      'uc':c/'opg169-s08-cycle4-universal-check.py',
      'ur':c/'opg169-s08-cycle4-universal-results.json',
      'ag':c/'opg169-s08-cycle4-anchored-generate.py',
      'ac':c/'opg169-s08-cycle4-anchored-check.py',
      'ar':c/'opg169-s08-cycle4-anchored-results.json',
    }

def main()->None:
    assert digest(SMALL['po'])==EXPECTED['po'];assert digest(SMALL['fo'])==EXPECTED['fo']
    with tempfile.TemporaryDirectory(prefix='opg169-s08-c4-') as td0:
        td=pathlib.Path(td0);files=reconstruct(td)
        assert digest(files['ur'])==EXPECTED['ur'];assert digest(files['ar'])==EXPECTED['ar']
        outdir=td/'run';outdir.mkdir();ur=outdir/'universal.json';ar=outdir/'anchored.json';po=outdir/'plane.json';fo=outdir/'anchors.json'
        run([PYTHON,str(files['ug']),str(ur)])
        if ur.read_bytes()!=files['ur'].read_bytes():raise AssertionError('universal regeneration mismatch')
        uc=run([PYTHON,str(files['uc']),str(ur)])
        run([PYTHON,str(files['ag']),str(ur),str(ar)])
        if ar.read_bytes()!=files['ar'].read_bytes():raise AssertionError('anchored regeneration mismatch')
        names=['P10','P11','P12','P13','P14','counterexample']
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            fut={name:pool.submit(run,[PYTHON,str(files['ac']),str(ar),name]) for name in names}
            modes={name:fut[name].result() for name in names}
        run([PYTHON,str(SMALL['pc']),str(po)])
        if po.read_bytes()!=SMALL['po'].read_bytes():raise AssertionError('plane output mismatch')
        anchors=run([PYTHON,str(SMALL['fc']),str(ar),str(fo)])
        if fo.read_bytes()!=SMALL['fo'].read_bytes():raise AssertionError('anchor output mismatch')
    out={
      'status':'ok','verdict':'candidate_only','universal_result_sha256':EXPECTED['ur'],
      'anchored_result_sha256':EXPECTED['ar'],'plane_output_sha256':EXPECTED['po'],
      'anchor_output_sha256':EXPECTED['fo'],'universal_rows':len(uc['rows']),
      'anchored_modes':sorted(modes),'possible_new_triangles':sum(len(v) for v in anchors['parents'].values()),
      'deleted_anchor_intersection':modes['counterexample']['counterexample']['intersection'],
      'root_closed':False,
    }
    print(json.dumps(out,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()

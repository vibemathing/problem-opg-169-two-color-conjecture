#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,hashlib,json,pathlib,subprocess,tempfile,zlib

ROOT=pathlib.Path(__file__).resolve().parents[3]
CAP=pathlib.Path(__file__).with_name("opg169-a01-c43-capsule.json")
GEO=pathlib.Path(__file__).with_name("opg169-a01-c43-c41-geometry.json")

def decode():
    c=json.loads(CAP.read_text())
    raw=zlib.decompress(base64.b64decode(c["zlib_b64"]))
    assert len(raw)==c["decoded_size"]
    assert hashlib.sha256(raw).hexdigest()==c["decoded_sha256"]
    files=json.loads(raw)
    assert len(files)==c["inner_file_count"]
    for n,s in files.items():
        assert hashlib.sha256(s.encode()).hexdigest()==c["inner_sha256"][n]
    return c,files

def audit():
    c,files=decode()
    return {"status":"ok","mode":"audit","files":len(files),
            "decoded_size":c["decoded_size"],"decoded_sha256":c["decoded_sha256"]}

def reproduce():
    c,files=decode()
    with tempfile.TemporaryDirectory() as td:
        p=pathlib.Path(td)
        for n,s in files.items():(p/n).write_text(s)
        (p/GEO.name).write_bytes(GEO.read_bytes())
        cmds=[
          ["python3",files_key(files,"geometry-check.py"),GEO.name],
          ["python3",files_key(files,"geometry-audit.py"),GEO.name],
        ]
        outs=[]
        for cmd in cmds:
            r=subprocess.run(cmd,cwd=p,capture_output=True,text=True,timeout=30)
            assert r.returncode==0 and not r.stderr
            outs.append(json.loads(r.stdout))
        src=files_key(files,"corrected-two-hole.cpp")
        exe=p/"twohole"
        r=subprocess.run(["g++","-std=c++20","-O2","-pipe",src,"-o",str(exe)],cwd=p,capture_output=True,text=True,timeout=30)
        assert r.returncode==0
        r=subprocess.run([str(exe)],cwd=p,capture_output=True,text=True,timeout=45)
        assert r.returncode==0 and not r.stderr
        assert hashlib.sha256(r.stdout.encode()).hexdigest()==c["inner_sha256"][files_key(files,"corrected-two-hole-output.json")]
        (p/files_key(files,"corrected-two-hole-output.json")).write_text(r.stdout)
        r2=subprocess.run(["python3",files_key(files,"corrected-two-hole-audit.py"),GEO.name,files_key(files,"corrected-two-hole-output.json")],
                          cwd=p,capture_output=True,text=True,timeout=120)
        assert r2.returncode==0 and not r2.stderr
        outs.append(json.loads(r2.stdout))
        assert all(x["status"]=="ok" for x in outs)
        return {"status":"ok","mode":"reproduce","files":len(files),
                "geometry_implementations":2,"two_hole_rows":72,"two_hole_successes":0}

def files_key(files,suffix):
    z=[n for n in files if n.endswith(suffix)]
    assert len(z)==1,(suffix,z)
    return z[0]

def main():
    ap=argparse.ArgumentParser();ap.add_argument("mode",choices=["audit","reproduce"],nargs="?",default="audit")
    a=ap.parse_args();print(json.dumps(audit() if a.mode=="audit" else reproduce(),sort_keys=True,separators=(",",":")))

if __name__=="__main__":main()

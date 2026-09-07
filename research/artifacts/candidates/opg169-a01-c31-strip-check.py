"""Finite controls for an all-exterior alternating-strip replacement.
No trusted-verifier authority; all arc sets are generated explicitly.
"""
import ctypes
import ctypes.util
import hashlib
import itertools
import json
import os
import platform
import resource
import signal
import sys
from pathlib import Path


def restrict_runtime():
    if platform.python_version() != '3.13.5':
        raise RuntimeError('CPython 3.13.5 required')
    resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))
    resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
    resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    signal.alarm(25)
    name = ctypes.util.find_library('seccomp')
    if not name:
        raise RuntimeError('libseccomp required')
    lib = ctypes.CDLL(name)
    lib.seccomp_init.argtypes = [ctypes.c_uint32]
    lib.seccomp_init.restype = ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes = [ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint]
    lib.seccomp_load.argtypes = [ctypes.c_void_p]
    lib.seccomp_release.argtypes = [ctypes.c_void_p]
    ctx = lib.seccomp_init(0x7fff0000)
    if not ctx:
        raise RuntimeError('seccomp init')
    for s in (b'socket', b'socketpair', b'connect'):
        call = lib.seccomp_syscall_resolve_name(s)
        if call < 0 or lib.seccomp_rule_add(ctx, 0x00050001, call, 0) != 0:
            raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx) != 0:
        raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)


def need(x, label):
    if not x:
        raise ValueError(label)


def closure(arcs, vs):
    r = {(a, b) for a, b in arcs if a in vs and b in vs}
    for z in sorted(vs):
        r |= {(a, b) for a in vs for b in vs if (a, z) in r and (z, b) in r}
    return r


def dag(arcs, vs):
    left = set(vs)
    while left:
        zero = {v for v in left if not any((u, v) in arcs for u in left)}
        if not zero:
            return False
        left -= zero
    return True


def graph(k, start):
    A = {(i + 2, i + 3) for i in range(k - 1)}
    for i in range(k):
        z = i + 2
        A |= {(0, z), (z, 1)} if (i + start) % 2 == 0 else {(1, z), (z, 0)}
    return A, (0, 2, 1, k + 1)


def embedding(A, k):
    z = list(range(2, k + 2))
    rotation = {0:z, 1:z[::-1], z[0]:[0,1,z[1]], z[-1]:[0,z[-2],1]}
    for i in range(1, k - 1):
        rotation[z[i]] = [0,z[i-1],1,z[i+1]]
    darts = A | {(b,a) for a,b in A}
    for x, ns in rotation.items():
        need(len(ns) == len(set(ns)) and set(ns) == {b for a,b in darts if a == x}, 'rotation neighbours')
    seen, faces = set(), []
    for edge in sorted(darts):
        if edge in seen:
            continue
        d, face = edge, []
        while d not in seen:
            seen.add(d)
            x,y = d
            face.append(x)
            ns = rotation[y]
            d = y,ns[(ns.index(x)+1)%len(ns)]
        need(d == edge,'face permutation')
        faces.append(face)
    need(k + 2 - len(A) + len(faces) == 2,'Euler sphere')
    need(sorted(len(f) for f in faces) == [3]*(2*k-2)+[4],'one quadrilateral outer face')
    B = [0,z[0],1,z[-1]]
    need(any(f == B[i:]+B[:i] or f == (B[i:]+B[:i])[::-1]
             for f in faces for i in range(4)), 'preserved labelled boundary order')
    return rotation, faces


def state(A, n, B, colour):
    R = set()
    for h in (0, 1):
        V = {x for x in range(n) if colour[x] == h}
        rp = closure(A, V)
        ok = dag(A, V)
        need(ok == (not any((x, x) in rp for x in V)), 'two cycle engines')
        if not ok:
            return None
        R |= {(B.index(x), B.index(y)) for x, y in rp if x in B and y in B}
    return tuple(colour[x] for x in B), tuple(sorted(R))


def symbolic(k, start):
    out = set()
    types = (start, (start + k - 1) % 2)
    internal = {(start + i) % 2 for i in range(1, k - 1)}
    for sig in itertools.product((0, 1), repeat=4):
        p, a, q, b = sig
        base = set()
        for z, typ in ((1, types[0]), (3, types[1])):
            for x, y in (((0, z), (z, 2)) if typ == 0 else ((2, z), (z, 0))):
                if sig[x] == sig[y]:
                    base.add((x, y))
        if p != q:
            if (a ^ p ^ types[0]) >= (b ^ p ^ types[1]):
                out.add((sig, tuple(sorted(closure(base, set(range(4)))))))
        else:
            forced = {typ for col, typ in ((a, types[0]), (b, types[1])) if col == p}
            if not forced:
                out.add((sig, ((1, 3),)))
            for typ in (0, 1):
                if forced <= {typ} and (typ in forced or typ in internal):
                    r = base | ({(0, 2)} if typ == 0 else {(2, 0)})
                    out.add((sig, tuple(sorted(closure(r, set(range(4)))))))
    return out


def main():
    restrict_runtime()
    report = {'verdict':'candidate_only','trusted_verifier_receipt':False,
              'complete':False,'runtime':platform.python_version(),
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'range':{'path_vertices':[3,4,5,6,7,8,9],'first_types':[0,1]},
              'cases':[],'replacements':[]}
    profiles = {}
    try:
        for start in (0, 1):
            for k in range(3, 10):
                A, B = graph(k, start)
                need(all(x != y and (y, x) not in A for x, y in A), 'orientation')
                rot, faces = embedding(A, k)
                prof, good = set(), 0
                for c in itertools.product((0, 1), repeat=k + 2):
                    s = state(A, k + 2, B, c)
                    if s is not None:
                        prof.add(s)
                        good += 1
                need(prof == symbolic(k, start), 'exact symbolic profile')
                profiles[k, start] = prof
                report['cases'].append({'path_vertices':k,'first_type':start,
                    'assignments':2**(k+2),'valid_colourings':good,'states':len(prof),
                    'arcs':sorted(A),'rotation':rot,'faces':faces})
                if k >= 6:
                    small = 4 if k % 2 == 0 else 5
                    need(prof == profiles[small, start], 'short-strip equivalence')
                    report['replacements'].append({'long':k,'short':small,'first_type':start,
                                                  'all_states_equal':True,'states':len(prof)})
        # Required regime that an odd path of length three cannot realize.
        missing = ((0, 1, 0, 1), ((0, 2),))
        need(missing in profiles[5, 0] and missing not in profiles[3, 0], 'three-vertex false shortcut')
        report['five_not_three_witness'] = {'boundary_colours':missing[0],'positive_relation':missing[1]}
        report['complete_profiles'] = {str(k)+'-'+str(s):sorted(profiles[k,s]) for k in (3,4,5) for s in (0,1)}
        report['complete'],report['status'] = True,'bounded_strip_controls_passed'
        code = 0
    except (ValueError,KeyError,TypeError) as e:
        report['status'],report['error'] = 'candidate_mismatch',str(e)
        code = 1
    text = json.dumps(report,sort_keys=True)
    need(len(text.encode()) < 65536,'output cap')
    print(text)
    return code


if __name__ == '__main__':
    sys.exit(main())

// R08 S02-B Cycle 3 — TERMINAL-USEFULNESS adversarial checker
// Candidate-only. Same-principal exhaustive finite control, not trusted verification.
//
// Family T_N (even N>=6):
//   poles U,D; rings A_i,B_i.
//   ring edges A_i A_{i+1}, B_i B_{i+1};
//   U-A_i, D-B_i;
//   cross A_i-B_i, A_i-B_{i-1}.
// Orientation (period two):
//   A-ring bit (0,1), B-ring bit (0,0),
//   U-spoke bit (0,1), D-spoke bit (0,1),
//   A_i-B_i bit (1,1), A_i-B_{i-1} bit (0,0).
//
// The checker proves in its finite combinatorial model:
//  * simple plane triangulation, min semidegree >=2, no nonfacial 3-cycle;
//  * an A-ring sweep has growing interface |B_t|=t+4;
//  * every consecutive A-block of size 1, 2, or 3 has NO strict
//    same-boundary ordinary extension replacement.
// For a k-block, every strict replacement with <k internal vertices is covered.
// Nonmaximal disks are dominated for this obstruction test by their arbitrary
// maximal triangulated completions: adding edges only shrinks the valid-Q set.

#include <bits/stdc++.h>
using namespace std;

using U64 = uint64_t;

static int edge_index(int a, int b) {
    if (a>b) swap(a,b);
    int idx=0;
    for (int i=0;i<9;i++) for (int j=i+1;j<9;j++,idx++)
        if (i==a && j==b) return idx;
    abort();
}
static U64 ebit(int a,int b){ return U64(1) << edge_index(a,b); }

static bool valid_coloring(const vector<uint16_t>& out, int mask) {
    const int n=(int)out.size();
    const int all=(1<<n)-1;
    for (int color=0;color<2;color++) {
        int S = color ? mask : (all^mask);
        int indeg[16]={0};
        for (int u=0;u<n;u++) if (S&(1<<u)) {
            uint16_t m=out[u] & S;
            while(m){ int v=__builtin_ctz((unsigned)m); m&=m-1; indeg[v]++; }
        }
        int q[16],h=0,t=0,seen=0;
        for(int v=0;v<n;v++) if((S&(1<<v)) && indeg[v]==0) q[t++]=v;
        while(h<t){
            int u=q[h++]; seen++;
            uint16_t m=out[u]&S;
            while(m){
                int v=__builtin_ctz((unsigned)m); m&=m-1;
                if(--indeg[v]==0) q[t++]=v;
            }
        }
        if(seen != __builtin_popcount((unsigned)S)) return false;
    }
    return true;
}

struct Family {
    int N, U, D;
    vector<pair<int,int>> arcs;
    vector<vector<int>> rot;
    vector<array<int,3>> faces;
};

static void add_arc(vector<pair<int,int>>& A,int x,int y,bool bit){
    A.push_back(bit ? make_pair(x,y) : make_pair(y,x));
}

static Family build_family(int N){
    if(N<6 || N%2) throw runtime_error("N must be even >=6");
    Family F; F.N=N; F.U=0; F.D=1;
    const int U=0,D=1;
    auto A=[&](int i){ i=(i%N+N)%N; return 2+i; };
    auto B=[&](int i){ i=(i%N+N)%N; return 2+N+i; };

    for(int i=0;i<N;i++){
        add_arc(F.arcs,A(i),A(i+1), (i&1) ? 1:0);  // Ac=(0,1)
        add_arc(F.arcs,B(i),B(i+1), 0);             // Bc=(0,0)
        add_arc(F.arcs,U,A(i),       (i&1) ? 1:0);  // U=(0,1)
        add_arc(F.arcs,D,B(i),       (i&1) ? 1:0);  // D=(0,1)
        add_arc(F.arcs,A(i),B(i),    1);             // C=(1,1)
        add_arc(F.arcs,A(i),B(i-1),  0);             // E=(0,0)
    }

    const int V=2*N+2;
    F.rot.assign(V,{});
    for(int i=0;i<N;i++) F.rot[U].push_back(A(i));
    for(int i=N-1;i>=0;i--) F.rot[D].push_back(B(i));
    for(int i=0;i<N;i++){
        F.rot[A(i)]={U,A(i-1),B(i-1),B(i),A(i+1)};
        F.rot[B(i)]={D,B(i+1),A(i+1),A(i),B(i-1)};
    }

    // Trace faces using the same rotation convention as prior S02-B checkers.
    set<pair<int,int>> darts;
    for(int v=0;v<V;v++) for(int w:F.rot[v]) darts.insert({v,w});
    while(!darts.empty()){
        auto start=*darts.begin(), d=start;
        vector<int> face;
        for(int guard=0;guard<10000;guard++){
            if(!darts.count(d)) throw runtime_error("rotation dart repeat");
            darts.erase(d);
            int u=d.first,v=d.second; face.push_back(u);
            auto &ns=F.rot[v];
            auto it=find(ns.begin(),ns.end(),u);
            if(it==ns.end()) throw runtime_error("asymmetric rotation");
            int pos=(int)(it-ns.begin());
            int w=ns[(pos+1)%ns.size()];
            d={v,w};
            if(d==start) break;
        }
        if(face.size()!=3) throw runtime_error("nontriangular face");
        F.faces.push_back({face[0],face[1],face[2]});
    }
    return F;
}

static void structural_check(int N){
    Family F=build_family(N);
    int V=2*N+2;
    set<pair<int,int>> Uedges;
    set<pair<int,int>> directed;
    vector<int> indeg(V,0),outdeg(V,0);
    for(auto [a,b]:F.arcs){
        if(a==b) throw runtime_error("loop");
        if(directed.count({a,b}) || directed.count({b,a}))
            throw runtime_error("duplicate/opposite underlying edge");
        directed.insert({a,b});
        Uedges.insert(minmax(a,b));
        outdeg[a]++; indeg[b]++;
    }
    if((int)Uedges.size()!=6*N) throw runtime_error("edge count");
    if((int)F.faces.size()!=4*N) throw runtime_error("face count");
    if(V-(int)Uedges.size()+(int)F.faces.size()!=2) throw runtime_error("Euler");
    if(*min_element(indeg.begin(),indeg.end())<2 ||
       *min_element(outdeg.begin(),outdeg.end())<2) throw runtime_error("semidegree");

    // Every 3-clique is one of the traced facial triangles.
    set<array<int,3>> face_sets;
    for(auto f:F.faces){ sort(f.begin(),f.end()); face_sets.insert(f); }
    vector<vector<char>> adj(V, vector<char>(V,0));
    for(auto [a,b]:Uedges) adj[a][b]=adj[b][a]=1;
    int triangles=0;
    for(int a=0;a<V;a++) for(int b=a+1;b<V;b++) if(adj[a][b])
        for(int c=b+1;c<V;c++) if(adj[a][c]&&adj[b][c]){
            triangles++;
            array<int,3> t{a,b,c};
            if(!face_sets.count(t)) throw runtime_error("nonfacial 3-cycle");
        }
    if(triangles!=4*N) throw runtime_error("triangle count");
}

struct Patch {
    int b, k;
    vector<pair<int,int>> arcs; // boundary vertices 0..b-1, internals b..b+k-1
    vector<int> boundary_global;
};

static Patch build_A_block(int N,int start,int k){
    Family F=build_family(N);
    auto A=[&](int i){ i=(i%N+N)%N; return 2+i; };
    set<int> centers;
    for(int j=0;j<k;j++) centers.insert(A(start+j));

    vector<array<int,3>> inc;
    for(auto f:F.faces)
        if(centers.count(f[0])||centers.count(f[1])||centers.count(f[2]))
            inc.push_back(f);

    map<pair<int,int>,int> ec;
    set<int> verts;
    for(auto f:inc){
        for(int x:f) verts.insert(x);
        for(int j=0;j<3;j++){
            auto e=minmax(f[j],f[(j+1)%3]);
            ec[e]++;
        }
    }
    map<int,vector<int>> badj;
    set<pair<int,int>> patch_edges;
    for(auto [e,c]:ec){
        patch_edges.insert(e);
        if(c==1){ badj[e.first].push_back(e.second); badj[e.second].push_back(e.first); }
    }
    for(auto [v,ns]:badj) if(ns.size()!=2) throw runtime_error("boundary not cycle");

    int s=badj.begin()->first, prev=-1, cur=s;
    vector<int> boundary{s};
    while(true){
        auto ns=badj[cur];
        int nxt = (ns[0]==prev ? ns[1] : ns[0]);
        if(nxt==s) break;
        boundary.push_back(nxt);
        prev=cur; cur=nxt;
        if(boundary.size()>1000) throw runtime_error("boundary trace");
    }

    vector<int> internals;
    set<int> Bset(boundary.begin(),boundary.end());
    for(int v:verts) if(!Bset.count(v)) internals.push_back(v);
    if((int)internals.size()!=k) throw runtime_error("internal count");

    map<int,int> mp;
    for(int i=0;i<(int)boundary.size();i++) mp[boundary[i]]=i;
    for(int i=0;i<k;i++) mp[internals[i]]=boundary.size()+i;

    vector<pair<int,int>> parcs;
    for(auto e:F.arcs)
        if(patch_edges.count(minmax(e.first,e.second)))
            parcs.push_back({mp[e.first],mp[e.second]});

    return Patch{(int)boundary.size(),k,parcs,boundary};
}

static vector<int> invalid_boundary_words(const Patch& P){
    int n=P.b+P.k;
    vector<uint16_t> out(n,0);
    for(auto [a,b]:P.arcs) out[a]|=1<<b;
    vector<int> invalid;
    for(int bm=0;bm<(1<<P.b);bm++){
        bool ok=false;
        for(int im=0;im<(1<<P.k);im++)
            if(valid_coloring(out,bm|(im<<P.b))){ ok=true; break; }
        if(!ok) invalid.push_back(bm);
    }
    return invalid;
}

static vector<int> boundary_bits(const Patch& P){
    set<pair<int,int>> A(P.arcs.begin(),P.arcs.end());
    vector<int> bits(P.b);
    for(int i=0;i<P.b;i++){
        int j=(i+1)%P.b;
        if(A.count({i,j})) bits[i]=1;
        else if(A.count({j,i})) bits[i]=0;
        else throw runtime_error("missing boundary arc");
    }
    return bits;
}

// Complete topology generator by root-face recursion.
// boundary is a cyclic polygonal chain whose closing edge is boundary.back()-boundary.front().
// The unique face on that closing edge has third vertex either on the boundary
// (splitting into two subdisks) or among the remaining interior vertices
// (that vertex becomes boundary of the remaining disk).
struct Key {
    vector<int> B;
    int I;
    bool operator<(Key const& o) const { return B!=o.B ? B<o.B : I<o.I; }
};
static map<Key, vector<U64>> memo;

static vector<U64> gen_raw(vector<int> B,int I){
    Key key{B,I};
    if(auto it=memo.find(key);it!=memo.end()) return it->second;
    set<U64> outs;
    int m=B.size();
    if(I==0 && m==2){
        outs.insert(ebit(B[0],B[1]));
    } else if(I==0 && m==3){
        outs.insert(ebit(B[0],B[1])|ebit(B[1],B[2])|ebit(B[2],B[0]));
    } else {
        int a=B.front(), z=B.back();
        // Third vertex on boundary.
        for(int j=1;j<m-1;j++){
            int t=B[j];
            for(int I1=I;; I1=(I1-1)&I){
                int I2=I^I1;
                vector<int> L(B.begin(),B.begin()+j+1);
                vector<int> R(B.begin()+j,B.end());
                auto X=gen_raw(L,I1), Y=gen_raw(R,I2);
                U64 tri=ebit(a,z)|ebit(a,t)|ebit(t,z);
                for(U64 x:X) for(U64 y:Y) outs.insert(x|y|tri);
                if(I1==0) break;
            }
        }
        // Third vertex is interior.
        for(int x=0;x<9;x++) if(I&(1<<x)){
            vector<int> NB=B; NB.push_back(x);
            auto R=gen_raw(NB,I^(1<<x));
            U64 tri=ebit(a,z)|ebit(a,x)|ebit(x,z);
            for(U64 r:R) outs.insert(r|tri);
        }
    }
    vector<U64> ret(outs.begin(),outs.end());
    memo[key]=ret;
    return ret;
}

static vector<U64> disk_topologies(int b,int q){
    vector<int> B(b); iota(B.begin(),B.end(),0);
    int I=0; for(int x=b;x<b+q;x++) I|=1<<x;
    auto raw=gen_raw(B,I);
    int target=3*(b+q)-3-b;
    vector<U64> ans;
    for(U64 E:raw) if(__builtin_popcountll(E)==target) ans.push_back(E);
    sort(ans.begin(),ans.end()); ans.erase(unique(ans.begin(),ans.end()),ans.end());
    return ans;
}

static bool q_extends_forbidden(
    int b,int q,U64 topology,const vector<int>& bbits,const vector<int>& invalid,
    long long &orient_count)
{
    U64 bedges=0;
    for(int i=0;i<b;i++) bedges |= ebit(i,(i+1)%b);
    vector<pair<int,int>> extra;
    for(int i=0;i<b+q;i++) for(int j=i+1;j<b+q;j++)
        if((topology&ebit(i,j)) && !(bedges&ebit(i,j))) extra.push_back({i,j});
    const int m=extra.size();
    for(int ob=0;ob<(1<<m);ob++){
        orient_count++;
        vector<uint16_t> out(b+q,0);
        for(int i=0;i<b;i++){
            int j=(i+1)%b;
            if(bbits[i]) out[i]|=1<<j; else out[j]|=1<<i;
        }
        for(int t=0;t<m;t++){
            auto [a,c]=extra[t];
            if((ob>>t)&1) out[a]|=1<<c; else out[c]|=1<<a;
        }

        // Ext(Q) subset Ext(P) iff every P-invalid boundary word is Q-invalid.
        bool all_forbidden=true;
        for(int bm:invalid){
            bool qvalid=false;
            for(int im=0;im<(1<<q);im++)
                if(valid_coloring(out,bm|(im<<b))){ qvalid=true; break; }
            if(qvalid){ all_forbidden=false; break; }
        }
        if(all_forbidden) return true; // A candidate smaller extension replacement exists.
    }
    return false;
}

static void check_block(int k,int start, map<string,long long>& totals){
    const int N=12; // enough to avoid wrap for k<=3 and realize both parities.
    Patch P=build_A_block(N,start,k);
    if(P.b!=k+4) throw runtime_error("unexpected growing boundary");
    vector<int> inv=invalid_boundary_words(P);
    vector<int> bits=boundary_bits(P);

    const int expected_ext[4]={0,24,46,86};
    int ext=(1<<P.b)-(int)inv.size();
    if(ext!=expected_ext[k]) throw runtime_error("unexpected P extension count");

    long long orientations=0;
    long long topology_count=0;
    for(int q=0;q<k;q++){
        auto tops=disk_topologies(P.b,q);
        topology_count += tops.size();

        // Frozen small topology counts are a canary for completeness of root-face recursion.
        if(P.b==5 && q==0 && tops.size()!=5) throw runtime_error("b5q0 topology count");
        if(P.b==6 && q==0 && tops.size()!=14) throw runtime_error("b6q0 topology count");
        if(P.b==6 && q==1 && tops.size()!=84) throw runtime_error("b6q1 topology count");
        if(P.b==7 && q==0 && tops.size()!=42) throw runtime_error("b7q0 topology count");
        if(P.b==7 && q==1 && tops.size()!=330) throw runtime_error("b7q1 topology count");
        if(P.b==7 && q==2 && tops.size()!=4620) throw runtime_error("b7q2 topology count");

        for(U64 E:tops){
            if(q_extends_forbidden(P.b,q,E,bits,inv,orientations))
                throw runtime_error("strict smaller ordinary-extension replacement found");
        }
    }

    string key="k"+to_string(k)+"_parity"+to_string(start&1);
    totals[key+"_boundary"]=P.b;
    totals[key+"_ext"]=ext;
    totals[key+"_invalid"]=inv.size();
    totals[key+"_topologies"]=topology_count;
    totals[key+"_Q_orientations"]=orientations;
}

int main(int argc,char**argv){
    int maxN=64;
    if(argc>=2) maxN=stoi(argv[1]);
    if(maxN<6) maxN=6;
    if(maxN%2) maxN--;

    for(int N=6;N<=maxN;N+=2) structural_check(N);

    // Exact growing-interface check for an A_0,...,A_{t-1} sweep.
    Family F=build_family(maxN);
    auto Aid=[&](int i){ i=(i%maxN+maxN)%maxN; return 2+i; };
    for(int t=1;t<=maxN-2;t++){
        set<int> C; for(int i=0;i<t;i++) C.insert(Aid(i));
        map<pair<int,int>,int> ec;
        for(auto f:F.faces) if(C.count(f[0])||C.count(f[1])||C.count(f[2]))
            for(int j=0;j<3;j++) ec[minmax(f[j],f[(j+1)%3])]++;
        set<int> bv;
        for(auto [e,c]:ec) if(c==1){ bv.insert(e.first); bv.insert(e.second); }
        if((int)bv.size()!=t+4) throw runtime_error("interface does not grow as t+4");
    }

    map<string,long long> totals;
    for(int k=1;k<=3;k++) for(int parity=0;parity<2;parity++) check_block(k,parity,totals);

    // Expected orientation totals per parity:
    // k1: 5 * 2^2 = 20
    // k2: 14*2^3 + 84*2^6 = 5,488
    // k3: 42*2^4 + 330*2^7 + 4620*2^10 = 4,773,792
    if(totals["k1_parity0_Q_orientations"]!=20 ||
       totals["k2_parity0_Q_orientations"]!=5488 ||
       totals["k3_parity0_Q_orientations"]!=4773792)
        throw runtime_error("orientation total canary");

    cout << "{";
    cout << "\"format\":\"opg169-s02b-cycle3-terminal-usefulness-v1\",";
    cout << "\"verdict\":\"candidate_only\",\"root_closed\":false,";
    cout << "\"family\":{";
    cout << "\"name\":\"period2_double_ring_T_N\",";
    cout << "\"checked_even_N_min\":6,\"checked_even_N_max\":"<<maxN<<",";
    cout << "\"vertices_at_max\":"<<(2*maxN+2)<<",";
    cout << "\"edges_at_max\":"<<(6*maxN)<<",";
    cout << "\"faces_at_max\":"<<(4*maxN)<<",";
    cout << "\"pole_degree\":"<<maxN<<",";
    cout << "\"min_semidegree\":2,";
    cout << "\"nonfacial_3cycles\":0,";
    cout << "\"A_sweep_unseen_after_N_minus_1\":1,";
    cout << "\"interface_formula\":\"|B_t|=t+4 for 1<=t<=N-2\"";
    cout << "},";
    cout << "\"block_obstruction\":{";
    bool first=true;
    for(auto [k,v]:totals){
        if(!first) cout<<","; first=false;
        cout<<"\""<<k<<"\":"<<v;
    }
    cout << "},";
    cout << "\"meaning\":{";
    cout << "\"ordinary_extension\":\"NO strict same-boundary replacement for every consecutive A-block of size <=3\",";
    cout << "\"strong_profile\":\"therefore also NO strong-profile replacement in those scopes\",";
    cout << "\"scope\":\"root-class high-port stress family; not an exact C37/LSRC/GSRC/JMAP descendant\",";
    cout << "\"next_open\":\"blocks of size >=4 or another nonlocal/source-specific useful terminal\"";
    cout << "}";
    cout << "}\n";
}

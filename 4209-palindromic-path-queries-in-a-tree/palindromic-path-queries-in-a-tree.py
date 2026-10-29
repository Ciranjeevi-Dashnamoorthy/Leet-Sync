
"""
Observation:

Brute Force:

  1) Build a adj list given the edges
  2) do dfs with depth and store the characters 
  3) for findig=ng the path between node u and v use 
     LCA with binary uplfiting
  
  Lagging:

  1) After a point update , updating the nodes in the tree and recalculating is difficult

  soln:
    
    maintain the charcters freqeuncy as bit

    final xor of all nodes has to be at most one 

    so maintain masks for each ndoe from the root

    FINAL MASK = mask of node u ^ mask of node v ^ char(LCA)

    to find lca --> binary uplifiting 
    to handle range queries and point updates --> fenwick tree

    most important is to flatten the tree --> using Euler path

"""
# Fenwick tree template
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+2)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] ^= val
            i += i & -i

    def query(self, i):
        ans = 0
        while i:
            ans ^= self.bit[i]
            i -= i & -i
        return ans

    def range_update(self, l, r, val):
        self.add(l, val)
        self.add(r+1, val)
    
# BINARY UPLIFTING
class BinaryLifting:
    def __init__(self, n, edges, root=1):
        self.n = n
        self.LOG = (n).bit_length()

        self.adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.depth = [0] * (n + 1)
        self.up = [[-1] * self.LOG for _ in range(n + 1)]

        self.dfs(root, -1)

    def dfs(self, node, parent):
        self.up[node][0] = parent

        for j in range(1, self.LOG):
            prev = self.up[node][j - 1]
            if prev != -1:
                self.up[node][j] = self.up[prev][j - 1]

        for nei in self.adj[node]:
            if nei != parent:
                self.depth[nei] = self.depth[node] + 1
                self.dfs(nei, node)

    # kth ancestor of node
    def kth_ancestor(self, node, k):
        for j in range(self.LOG):
            if node == -1:
                break
            if k & (1 << j):
                node = self.up[node][j]
        return node

    # Lowest Common Ancestor
    def lca(self, u, v):

        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # bring to same depth
        u = self.kth_ancestor(u, self.depth[u] - self.depth[v])

        if u == v:
            return u

        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        return self.up[u][0]

    # distance between two nodes
    def distance(self, u, v):
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:

        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #  Euler path
        
        tin=[0]*n
        tout=[0]*n
        self.timer=0

        def dfs(u,p):

            self.timer+=1
            tin[u]=self.timer

            for nei in adj[u]:
                if nei!=p:
                    dfs(nei,u)
            
            tout[u]=self.timer
        
        dfs(0,-1)

        bl=BinaryLifting(n,edges,0)

        bit=BIT(n)

        ch=list(s)

        for u in range(n):
            mask=1<<(ord(ch[u])-ord("a"))
            bit.range_update(tin[u],tout[u],mask)
        
        ans=[]

        for  q in queries:
            parts=q.split()

            if parts[0]=="update":
                u,c=int(parts[1]),parts[2]
                old=ch[u]

                if old!=c:
                    mask=(
                        (1<<(ord(c)-ord("a")))
                        ^ 
                        (1<<(ord(old)-ord("a")))
                        )
                    bit.range_update(tin[u],tout[u],mask)
                
                ch[u]=c
            else:
                u,v=int(parts[1]),int(parts[2])

                w=bl.lca(u,v)
            

                lca_mask=1<<(ord(ch[w])-ord("a"))
                u_mask=bit.query(tin[u])
                v_mask=bit.query(tin[v])
                req_mask= v_mask^u_mask^lca_mask

                if (req_mask==0) or (req_mask & (req_mask-1))==0 :
                    ans.append(True)
                else:
                    ans.append(False)
        return ans




        
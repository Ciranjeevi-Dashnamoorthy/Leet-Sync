class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        adj=[[] for _ in range(n)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        counted=set()
        if n==1:
            return 1
        self.ct=0
        def dfs(node):
           
            vis.add(node)
            val=values[node]

            for nei in adj[node]:
              if nei not in vis: 
                val+=dfs(nei)
            if val%k==0:
                self.ct+=1
                return 0
            return val
       
        for i in range(n):
            if i not in vis:
                dfs(i)
                
        return self.ct

        
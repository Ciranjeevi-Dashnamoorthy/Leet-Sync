class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n=len(edges)
        maxi=-1
        adj=[[] for _ in range(n)]
        for i in range(n):
            if edges[i]!=-1:
                adj[i].append(edges[i])
        rank=[-1]*n
        state=[0]*n
        def dfs(node,curr):
            nonlocal maxi
            rank[node]=curr
            state[node]=1
            for nei in adj[node]:
                if state[nei]==0:
                    dfs(nei,curr+1)
                elif state[nei]==1:
                    d=curr-rank[nei]+1
                    maxi=max(maxi,d)
            state[node]=2
        
        for i in range(n):
            if state[i]==0:
                dfs(i,0)
        return maxi
        
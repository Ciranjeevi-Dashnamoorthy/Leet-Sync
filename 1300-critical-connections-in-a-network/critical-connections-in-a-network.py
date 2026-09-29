class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:

        adj=[[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        rank=[-1]*n
        ans=[]

        def dfs(node,par,curr):

            rank[node]=curr
            lowest=curr

            for nei in adj[node]:
                if nei==par:
                    continue
                if rank[nei]==-1:
                    low=dfs(nei,node,curr+1)
                    if low>curr:
                        ans.append([node,nei])

                    lowest=min(lowest,low)
                else:
                    lowest=min(lowest,rank[nei])
            return lowest
        

        dfs(0,-1,0)
        return ans 
        
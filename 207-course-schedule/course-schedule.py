class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        
        adj=[[] for _ in range(n)]

        for u,v in pre:
            adj[u].append(v)
        state=[0]*n
        def dfs(node):

            if state[node]!=0:
                if state[node]==1:
                    return False
                else:
                    return True
            state[node]=1
            for nei in adj[node]:
                if state[nei]==1 or not dfs(nei):
                    return False
            
            state[node]=2
            return True
        

        for i in range(n):
            if not dfs(i):
                return False
        return True
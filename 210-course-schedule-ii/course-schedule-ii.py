class Solution:
    def findOrder(self, n: int, nums: List[List[int]]) -> List[int]:
        
        adj=[[] for _ in range(n)]
        for u,v in nums:
            adj[u].append(v)
        stack=[]
        state=[0]*n
        vis=set()
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            state[node]=2
            stack.append(node)
            return True
        

        for node in range(n):
            if state[node]==0:
                if not dfs(node):
                    return []
        
        
        return stack
       
        
        
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:

        """
        find the cycle in directed graph using 0,1,2 technique

        dfs(node) return the curr node leads to cycle or not 

        """

        n=len(graph)
        state=[0]*n 
        def dfs(node):

            if state[node]!=0:
                if state[node]==1:
                    return False
                else:
                    return  True

            state[node]=1

            for nei in graph[node]:
                if state[nei]==1 or not dfs(nei):
                    return False
            
            state[node]=2
            return True

        res=[]
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:

        n=len(graph)
        color=[-1]*n 
        
        def dfs(node,col):

            color[node]=col
            if col==0:
                op=1
            else:
                op=0

            for nei in graph[node]:
                if color[nei]==-1:
                    if not dfs(nei,op):
                        return False
                else:
                    if color[nei]==col:
                        return False
            return True
        
        for node in range(n):
            if color[node]==-1:
                if not dfs(node,0):
                    return False
        return True
            
        
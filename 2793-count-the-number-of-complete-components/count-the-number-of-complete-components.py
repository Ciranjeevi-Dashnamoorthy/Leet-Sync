class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        adj=[[] for _ in range(n)]

        degree=[0]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1

        
        ct=0
        components=[]
        vis=set()
    
        for i in range(n):
            
            node=i
            curr=[]
            stack=[]
            
            if node not in vis:
                vis.add(node)
                stack.append(node)
                curr.append(node)

            while stack:
                curr_node=stack.pop()
                for nei in adj[curr_node]:
                    if nei not in vis:
                        vis.add(nei)
                        stack.append(nei)
                        curr.append(nei)
            if curr:
                components.append(curr)
    
        for comp in components:
            
            target=len(comp)-1
            fl=True
            for node in comp:

                if target!=degree[node]:
                    fl=False
                    break
            if fl:
                ct+=1
            
        return ct
                
        
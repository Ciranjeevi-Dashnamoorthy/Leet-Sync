class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        import heapq
        from collections import deque
        
        adj=[[] for _ in range(n)]

        for i in range(len(edges)):
            u,v,w=edges[i]
            adj[u].append((v,w,i))
            adj[v].append((u,w,i))
        
        dist=[float("inf")]*n
        dist[0]=0
        heap=[(0,0)]

        while heap:
            cost,node=heapq.heappop(heap)

            for dest,weight,_ in adj[node]:
                curr=cost+weight
                if curr<dist[dest]:
                    dist[dest]=curr
                    heapq.heappush(heap,(curr,dest))
        
        queue=deque()
        queue.append(n-1)
        visited=set()
        visited.add(n-1)
        m=len(edges)
        res=[False]*m
        if dist[-1]==float("inf"):
            return res
       

        while queue:
            node=queue.popleft()

            for nei,weight,idx in adj[node]:
                if dist[nei]+weight==dist[node]:
                    res[idx]=True
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        return res
                    

                
            
        
        



        
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
       

        """
        0- Red 
        1- Blue
        """
        
        
        blue=[[] for _ in range(n)]
        red=[[] for _ in range(n)]
        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        
    
        ans=[-1]*n

        queue=deque([(0,0,1),(0,0,0)])
        vis=set()
        vis.add((0,1))
        vis.add((0,0))

        while queue:

            node,dist,prev=queue.popleft()

            if ans[node]==-1:
                ans[node]=dist

            if prev==0:

                for nei in red[node]:
                    
                    if (nei,1) not in vis:
                        queue.append((nei,dist+1,1))
                        vis.add((nei,1))
            else:
                for nei in blue[node]:
                    
                    if (nei,0) not in vis:
                        queue.append((nei,dist+1,0))
                        vis.add((nei,0))
        return ans
            

        
        
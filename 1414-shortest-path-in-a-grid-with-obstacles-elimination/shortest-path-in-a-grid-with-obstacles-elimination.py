class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        """
        Observation:

        DO BFS and keep track of attackes used for every step
        """

        from collections import deque

        m,n=len(grid),len(grid[0])

        queue=deque([(0,0,0,0)])
        vis=set()
        vis.add((0,0,0))
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:

            r,c,steps,used=queue.popleft()

            if r==m-1 and c==n-1:
                return steps
          
            
            for i,j in dirs:
                nr,nc=r+i,c+j
                if 0<=nr<m and 0<=nc<n:
                    new_used=used
                    if grid[nr][nc]==1:
                            new_used+=1
                    if new_used<=k and (nr,nc,new_used) not in vis:
                        
                        queue.append((nr,nc,steps+1,new_used))
                        vis.add((nr,nc,new_used))
        return -1
            

        
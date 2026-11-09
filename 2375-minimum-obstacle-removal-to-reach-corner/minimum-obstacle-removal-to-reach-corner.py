from collections import deque
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:

        heap=[(0,0,0)]
        vis=set((0,0))
        m,n=len(grid),len(grid[0])

        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        while heap:
            cost,r,c=heapq.heappop(heap)
            if r==m-1 and c==n-1:
                return cost
            for i,j in dirs:
                nr,nc=r+i,c+j
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in vis:
                    val=0
                    vis.add((nr,nc))
                    if grid[nr][nc]==1:
                        val=1
                    heapq.heappush(heap,(cost+val,nr,nc))
        
                    


        
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        vis=set()
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            vis.add((r,c))
            
            fl=True
            for i,j in dirs:
                nr,nc=i+r,j+c
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==0 and (nr,nc)not in vis:
                    if not dfs(nr,nc):
                        fl=False
            if r==0 or r==m-1 or c==n-1 or c==0:
                return False

            return fl

        n=len(grid[0])
        m=len(grid)
        ct=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and (i,j) not in vis:

                    if dfs(i,j):
                        ct+=1
                    
        return ct
        
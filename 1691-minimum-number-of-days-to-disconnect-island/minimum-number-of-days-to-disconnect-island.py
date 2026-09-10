class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        m,n=len(grid),len(grid[0])
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        
        

        def dfs(r,c,s):

            s.add((r,c))
            check=0
            for i,j in dirs:
                nr,nc=i+r,j+c
                
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1 and (nr,nc) not in s:
                    dfs(nr,nc,s)
        
        def check():
            s=set()
            ct=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and (i,j) not in s:
                        dfs(i,j,s)
                        ct+=1
            return ct

        if check()!=1:
            return 0    
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if check()!=1:
                        return 1
                    
                    grid[i][j]=1
        
        return 2
        

        
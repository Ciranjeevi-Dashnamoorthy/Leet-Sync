class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid),len(grid[0])
        mod=10**9 + 7

        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1

        def check(r,c):
            if 0<=r<m and 0<=c<n:
                return True
            return False
        
        dirs=[(0,1),(1,0)]
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]==1:
                    continue
            
                if check(i-1,j):
                    dp[i][j]=(dp[i][j]+dp[i-1][j])%mod
                if check(i,j-1):
                    dp[i][j]=(dp[i][j]+dp[i][j-1])%mod
                if i+1<m and grid[i+1][j]==1:
                    down=False
                    dr,dc=dirs[down]
                    nr,nc=i+dr+1,dc+j
                 
                    while check(nr,nc) and grid[nr][nc]==1:
                        down= not down
                        dr,dc=dirs[down]
                        prevr,prevc=nr,nc
                        nr,nc=prevr+dr,prevc+dc
                     
                    if check(nr,nc):
                        dp[nr][nc]=(dp[nr][nc]+dp[i][j])%mod
                
                if j+1<n and grid[i][j+1]==1:
                    down=True
                    dr,dc=dirs[down]
                    nr,nc=i+dr,dc+j+1
                  
                    while check(nr,nc) and grid[nr][nc]==1:
                        down= not down
                        dr,dc=dirs[down]
                        prevr,prevc=nr,nc
                        nr,nc=prevr+dr,prevc+dc
                        
                    if check(nr,nc):
                        dp[nr][nc]=(dp[nr][nc]+dp[i][j])%mod
                
               
        return dp[m-1][n-1]

        
        
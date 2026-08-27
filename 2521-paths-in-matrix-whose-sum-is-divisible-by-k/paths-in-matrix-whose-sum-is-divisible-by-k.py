class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        m=len(grid)
        n=len(grid[0])

        dp=[[[0]*k for _ in range(n) ]for _ in range(m)]
        dp[0][0][grid[0][0]%k]=1
        mod=10**9+7 
        curr=grid[0][0]
        for i in range(1,n):
            curr+=grid[0][i]
            rem=(curr)%k
            dp[0][i][rem]=1
        curr=grid[0][0]
        for i in range(1,m):
            curr+=grid[i][0]
            rem=(curr)%k
            dp[i][0][rem]=1
        
    

        for i in range(1,m):
            for j in range(1,n):
                for rem in range(k):

                    curr=(rem+grid[i][j])%k
                    
                    dp[i][j][curr]=(dp[i][j][curr]+dp[i-1][j][rem])%mod

                    curr=(rem+grid[i][j])%k
                  
                    dp[i][j][curr]=(dp[i][j][curr]+dp[i][j-1][rem])%mod
        

        return dp[m-1][n-1][0]
                

        
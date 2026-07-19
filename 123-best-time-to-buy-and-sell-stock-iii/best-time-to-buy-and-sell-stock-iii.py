class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        dp[0][1][1]=-prices[0]
        dp[0][1][2]=-prices[0]
        
        for i in range(1,n):
            for j in range(2):
                for k in range(1,3):
                
                    if j==0:
                        dp[i][j][k]=max(dp[i-1][0][k],dp[i-1][1][k]+prices[i])
                    else:
                        dp[i][j][k]=max(dp[i-1][1][k],dp[i-1][0][k-1]-prices[i])
        
        return dp[n-1][0][2]



         
            
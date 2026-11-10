class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n==1:
            return costs[0]+1
        if n==2:
            return min(costs[0]+1+costs[1]+1,costs[1]+4)        
        dp=[0]*(n+1)
        dp[1]=costs[0]+1
        dp[2]=min(costs[0]+1+costs[1]+1,costs[1]+4)  
    
        for i in range(3,n+1):
            dp[i]=min(dp[i-3]+costs[i-1]+9,dp[i-2]+costs[i-1]+4,dp[i-1]+costs[i-1]+1)
        
        
        return dp[n]
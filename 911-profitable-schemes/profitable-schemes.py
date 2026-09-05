class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        mod=10**9 + 7
        dp=[[0]*(minProfit+1) for _ in range(n+1)]
        dp[0][0]=1
       
        for i in range(len(group)):
            g=group[i]
            p=profit[i]

            for j in range(n,g-1,-1):
                for k in range(minProfit,-1,-1):

                    nex=k+p
                    if nex>minProfit:
                        nex=minProfit
                    
                    dp[j][nex]=(dp[j][nex]+dp[j-g][k])%mod
        
        ans=0
        for i in range(n+1):
            ans=(ans+dp[i][minProfit])%mod
        return ans
                

        
        
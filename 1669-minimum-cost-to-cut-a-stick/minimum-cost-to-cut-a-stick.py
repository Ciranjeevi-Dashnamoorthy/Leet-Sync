class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        """
        """

        
        cuts=[0]+cuts+[n]
        cuts.sort()
        m=len(cuts)

        dp=[[0]*(m) for _ in range(m)]

        for l in range(2,m):
            for i in range(m-l):
                j=i+l
                mini=float("inf")

                for k in range(i+1,j):
                    ans=cuts[j]-cuts[i]+ dp[i][k]+ dp[k][j]
                    mini=min(mini,ans)
                
                dp[i][j]=mini
        return dp[0][m-1]
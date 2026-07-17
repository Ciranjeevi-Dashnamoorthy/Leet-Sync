class Solution:
    def minCut(self, s: str) -> int:

        n=len(s)
        
        dp=[[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True

        ans=[0]*n
        for i in range(n):

            if dp[0][i]:
                ans[i]=0
            else:
                ans[i]=i

                for j in range(i+1):
                    
                    if dp[j][i]:
                        ans[i]=min(ans[i],ans[j-1]+1)
        return ans[-1]


                
    
        
        
        
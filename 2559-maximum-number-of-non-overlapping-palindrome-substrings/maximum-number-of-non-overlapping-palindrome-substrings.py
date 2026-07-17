class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n=len(s)
        dp=[[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
        
        ans=[0]*(n+1)

        for i in range(k,n+1):
            ans[i]=ans[i-1]
            
            for j in range(1,i-k+2):
               
                if dp[j-1][i-1]:
                    ans[i]=max(ans[i],ans[j-1]+1)
      
        return ans[-1]
        
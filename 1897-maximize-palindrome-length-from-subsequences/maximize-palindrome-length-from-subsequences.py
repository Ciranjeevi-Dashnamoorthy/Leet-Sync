class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:

        p,q=len(word1),len(word2)
        
        s=word1+word2
        rev=s[::-1]
        n=p+q

        dp=[[0]*(n) for _ in range(n)]

        for i in range(n):
            dp[i][i]=1

        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        maxi=0
        
        for i in range(p):
            for j in range(p,n):

                if s[i]==s[j]:
                
                    curr=2+dp[i+1][j-1]
                    maxi=max(maxi,curr)
        return maxi

        
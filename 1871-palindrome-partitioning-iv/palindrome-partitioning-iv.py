class Solution:
    def checkPartitioning(self, s: str) -> bool:

        """
        precompute palindrome and use brute force

        """
        n=len(s)

        dp=[[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
        
        ans=[0]*(n)
        for i in range(n-2):
            if dp[0][i]:
                for j in range(i+1,n-1):
                    if dp[i+1][j] and dp[j+1][n-1]:
                        return True
        
        return False

        
        
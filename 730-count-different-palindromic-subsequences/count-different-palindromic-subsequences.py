class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:

        """
        INTERVAL DP WITH EXTREME OBSERVATION

        maintain dp[i][j] --> count of diff palindrome

        if s[i]!=s[j] --> count using inclusion exclusion 

        else:
            to prevent duplicate addition
            check for the first and last occurence of the curr character

            if the curr character doesnt present means 
            curr+=2
            if exactly on means
            curr+=1

            else:
            
                curr- dp[left][right] where left , right id the first and last index

        """
        n=len(s)
        mod=10**9 + 7
        
        dp=[[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i]=1
        
        for l in range(2,n+1):
            for i in range(n-l+1):
                j=i+l-1
                
                if s[i]!=s[j]:
                    dp[i][j]=(dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1])%mod
                else:
                    left=i+1
                    right=j-1

                    while left<=right and s[left]!=s[i]:
                        left+=1

                    while left<=right and s[right]!=s[i]:
                        right-=1

                    if left>right:
                        dp[i][j]=(2*dp[i+1][j-1]+2)%mod 

                    elif left==right:
                        dp[i][j]=(2*dp[i+1][j-1]+1)%mod 
                    else:
                        dp[i][j]=(2*dp[i+1][j-1]-dp[left+1][right-1])%mod

        return dp[0][n-1]

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n=len(s)

        dp=[0]*26
        for i in range(n):
            curr=ord(s[i])-ord("a")
            maxi=0
            for j in range(curr-k,curr+k+1):
                if 0<=j and j<26:
                    maxi=max(maxi,dp[j]+1)
            dp[curr]=maxi
        return max(dp)
            
        
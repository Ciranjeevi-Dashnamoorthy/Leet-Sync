class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        """
        similar to LIS
        but in LIS we have to brute it for all poss val
        but here we havce only 26 options so comapring all those
        wont end in tle
        
        """
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
            
        
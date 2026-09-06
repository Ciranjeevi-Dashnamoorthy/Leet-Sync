class Solution:
    def distinctSubseqII(self, s: str) -> int:
        from collections import defaultdict
        d=defaultdict(int)
        mod=10**9 + 7

        n=len(s)
        dp=[0]*(n+1)
       
        
        
        for i in range(1,n+1):
            if s[i-1] not in d:
                dp[i]=(2*dp[i-1]+1)%mod
                d[s[i-1]]=i
            else:
                dp[i]=( 2*dp[i-1]- dp[d[s[i-1]]-1] )%mod
                d[s[i-1]]=i
        print(dp)
        return dp[-1]
                        
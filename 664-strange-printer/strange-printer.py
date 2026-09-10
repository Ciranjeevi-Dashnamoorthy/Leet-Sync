class Solution:
    def strangePrinter(self, s: str) -> int:

        n=len(s)
        @cache
        def dp(l,r):
            if l>r:
                return 0
            
            while l+1<n and s[l]==s[l+1]:
                l+=1
            
            ans=1+dp(l+1,r)
            for m in range(l+1,r+1):
                if s[l]==s[m]:
                    ans=min(ans,dp(l+1,m-1)+dp(m,r))
            return ans
        
        return dp(0,n-1)


        
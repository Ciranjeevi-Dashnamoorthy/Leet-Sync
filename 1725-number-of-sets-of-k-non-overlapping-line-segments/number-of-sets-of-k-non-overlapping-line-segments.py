class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod=10**9 + 7

        @cache
        def dp(idx,seg,fl):

            if seg==0:
                return 1
            if idx==n:
                return 0
            
            ans=dp(idx+1,seg,fl)
            if fl:
                ans+=dp(idx+1,seg,False)
            else:
                ans+=dp(idx,seg-1,True)
            return ans%mod
            
        return dp(0,k,True)
        
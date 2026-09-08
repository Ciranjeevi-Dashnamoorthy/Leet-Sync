class Solution:
    def removeBoxes(self, nums: List[int]) -> int:

        n=len(nums)
        @cache
        def dp(l,r,k):

            if l>r:
                return 0
            
            while l+1<=r and nums[l+1]==nums[l]:
                l+=1
                k+=1
            
            ans=(k+1)*(k+1)+dp(l+1,r,0)
            
            for m in range(l+1,r+1):
                if nums[l]==nums[m]:
                    ans=max(ans,dp(l+1,m-1,0)+dp(m,r,k+1))
            
            return ans
            
        

        return dp(0,n-1,0)
        
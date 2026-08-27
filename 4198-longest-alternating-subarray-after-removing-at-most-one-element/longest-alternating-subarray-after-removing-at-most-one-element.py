class Solution:
    def longestAlternating(self, nums: List[int]) -> int:

        """
        Observation:

        we use prefix and suffic dp for evry index r in 1,n-1

        
        """

        n=len(nums)
        inc=[1]*n
        dec=[1]*n
        ans=1

        for i in range(1,n):
            if nums[i-1]<nums[i]:
                inc[i]=dec[i-1]+1
            elif nums[i-1]>nums[i]:
                dec[i]=inc[i-1]+1
            ans=max(ans,inc[i],dec[i])
        
        right_inc=[1]*n
        right_dec=[1]*n

        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                right_inc[i]=right_dec[i+1]+1
            elif nums[i]>nums[i+1]:
                right_dec[i]=right_inc[i+1]+1
        
        for i in range(1,n-1):
            if nums[i-1]>nums[i+1]:
                ans=max(ans,inc[i-1]+right_inc[i+1])
            elif nums[i-1]<nums[i+1]:
                ans=max(ans,dec[i-1]+right_dec[i+1])
        return ans


        

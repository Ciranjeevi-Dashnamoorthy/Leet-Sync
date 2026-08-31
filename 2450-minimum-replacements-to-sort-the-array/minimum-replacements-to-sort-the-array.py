class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        n=len(nums)
        ops=0

        for i in range(n-2,-1,-1):
            if nums[i+1]<nums[i]:
                box=(nums[i]+nums[i+1]-1)//nums[i+1] 
                ops+=box-1
                lower=nums[i]//box
                nums[i]=lower
        return ops

                
        return ops

                 
        
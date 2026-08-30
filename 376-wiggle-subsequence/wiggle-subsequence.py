class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        u,d=1,1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                u=d+1
            if nums[i]<nums[i-1]:
                d=u+1
        return max(u,d)
            

            
        
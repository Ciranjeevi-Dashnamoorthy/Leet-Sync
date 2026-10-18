class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        n=len(nums)
        max1=max(nums)
        curr=0
        for i in range(n):
            curr=max(nums[i],curr+nums[i])
            max1=max(curr,max1)
        min1=float("inf")
        curr=0
        for i in range(n):
            curr=min(nums[i],curr+nums[i])
            min1=min(curr,min1)
       
        if max1<0:
            return max1
        return max(max1,sum(nums)-min1)


        
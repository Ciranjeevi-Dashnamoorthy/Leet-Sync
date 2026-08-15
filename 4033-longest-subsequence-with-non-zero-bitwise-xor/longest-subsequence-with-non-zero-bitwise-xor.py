class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        curr=0
        for i in range(n):
            curr^=nums[i]
        if sum(nums)==0:
            return 0
        if curr==0:
            return n-1
        elif curr>0:
            return n
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
    
        
        ops=0
        nums.sort()
        mid=nums[len(nums)//2]
        for i in range(len(nums)):
            ops+=abs(mid-nums[i])
        return ops
        
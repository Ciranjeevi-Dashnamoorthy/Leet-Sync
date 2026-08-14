class Solution:
    def minOperations(self, nums: List[int]) -> int:

        one=False
        n=len(nums)
        ops=0
        for i in range(n):
            if nums[i]==0 and not one:
                ops+=1
                one=True
            if nums[i]==1 and one:
                ops+=1
                one=False
        return ops
            
        
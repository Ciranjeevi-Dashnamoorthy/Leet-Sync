class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        s=0
        for num in nums:
            s+=abs(m-num)
        return s

        
        
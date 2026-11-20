class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        
        nums.sort()
        n=len(nums)
        dp=collections.defaultdict(int)
        for i in range(n):
            dp[nums[i]+1]=dp[nums[i]]+1
            dp[nums[i]]=dp[nums[i]-1]+1
        return max(dp.values())
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        from collections import defaultdict

        n=len(nums)

        dp=[defaultdict(int) for _ in range(n)]
        total=0

        for i in range(1,n):
            for j in range(i):

                diff=nums[i]-nums[j]
                count=dp[j][diff]
                total+=count

                dp[i][diff]+=count+1
        return total
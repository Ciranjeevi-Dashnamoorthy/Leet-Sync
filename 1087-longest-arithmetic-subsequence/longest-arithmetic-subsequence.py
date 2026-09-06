class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n=len(nums)

        dp=[[1]*1002 for _ in range(n)]
        maxi=0
     
        for i in range(1,n):
            for j in range(i):
                diff=nums[i]-nums[j]
                if diff<0:
                    diff=abs(diff)+500
                dp[i][diff]=max(dp[i][diff],dp[j][diff]+1)
                if maxi<dp[i][diff]:
                        maxi=dp[i][diff]
        return maxi


        
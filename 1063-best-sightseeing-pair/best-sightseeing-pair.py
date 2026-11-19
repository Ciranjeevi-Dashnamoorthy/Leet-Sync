class Solution:
    def maxScoreSightseeingPair(self, nums: list[int]) -> int:

        n=len(nums)
        ans=0
        curr=nums[0]-1

        for i in range(1,n):
            val=curr+nums[i]
            ans=max(val,ans)
            curr=max(curr,nums[i])
            curr-=1

        return ans

            
        
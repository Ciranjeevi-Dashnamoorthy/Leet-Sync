class Solution:
    def maxScoreSightseeingPair(self, nums: list[int]) -> int:

        n=len(nums)
        heap=[(-nums[0],0)]
        import heapq
        ans=0
        curr=nums[0]-1

        for i in range(1,n):
            val=curr+nums[i]-1
            ans=max(val,ans)
            curr=max(curr,nums[i])
            curr-=1

        return ans+1

            
        
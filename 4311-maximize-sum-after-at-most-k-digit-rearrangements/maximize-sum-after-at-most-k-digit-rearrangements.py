class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        import heapq
        nums.sort(reverse=True)
        n=len(nums)
        heap=[]

        for i in range(n):
            curr=list(str(nums[i]))
            curr.sort(reverse=True)
            val=int("".join(curr))
            diff=val-nums[i]
            heapq.heappush(heap,-diff)
        ans=0
        for i in range(k):
            val=-heapq.heappop(heap)
            if val<0:
                break
            ans+=val
        return ans+sum(nums)

            



        
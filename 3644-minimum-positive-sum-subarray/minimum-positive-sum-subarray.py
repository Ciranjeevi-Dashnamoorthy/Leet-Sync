class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        i,j=0,0
        n=len(nums)
        mini=float("inf")
        curr=0
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr+=nums[j]

                if j-i+1>r:
                    break
                if l<=j-i+1<=r and curr>0:
                    mini=min(mini,curr)
        return mini if mini!=float("inf") else -1



            

        
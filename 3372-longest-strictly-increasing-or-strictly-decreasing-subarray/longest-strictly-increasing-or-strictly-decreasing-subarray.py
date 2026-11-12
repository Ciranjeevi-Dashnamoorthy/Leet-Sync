class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n,ans,inc,dec=len(nums),0,1,1
        if n==1:
            return 1
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                inc+=1
                dec=1
            elif nums[i]>nums[i+1]:
                dec+=1
                inc=1
            else:
                dec=inc=1
            ans=max(inc,dec,ans)
        return ans

            
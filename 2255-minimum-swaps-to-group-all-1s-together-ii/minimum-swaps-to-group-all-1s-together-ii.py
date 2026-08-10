class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n=len(nums)

        one=nums.count(1)
        if one==0:
            return 0
        nums=nums+nums
        l=0
        curr=0
        ans=float("inf")
        for r in range(n+one-1):
            if nums[r]==1:
                curr+=1
            
            while r-l+1>one:
                if nums[l]==1:
                    curr-=1
                l+=1
        
            if r-l+1==one:
                ans=min(ans,r-l+1-curr)
        
        return ans




        
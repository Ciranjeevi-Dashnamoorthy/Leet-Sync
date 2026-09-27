class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        
        n=len(nums)
        ans=0
        for i in range(n):
            s=set()
            curr=0
            for j in range(i,n):
                curr+=nums[j]
                mod=(2*nums[j])%k
                s.add(mod)

                target=curr%k
                if target==0 or target in s:
                    ans=max(ans,j-i+1)
        return ans

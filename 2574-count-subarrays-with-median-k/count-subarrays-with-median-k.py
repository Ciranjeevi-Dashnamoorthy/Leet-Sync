class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        from collections import defaultdict
        d=defaultdict(int)
        curr=0
        d[0]=1
        ans=0
        fl=False

        for i in range(n):
            if nums[i]<k:
                curr-=1
            elif nums[i]>k:
                curr+=1
            else:
                fl=True
            
            if fl:
                ans+=d[curr]
                ans+=d[curr-1]
            else:
                d[curr]+=1
    
        return ans

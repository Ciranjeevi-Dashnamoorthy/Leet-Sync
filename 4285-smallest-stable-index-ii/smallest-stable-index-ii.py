class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)

        maxi=[0]*n
        mini=[0]*n
        m=0
        for i in range(n):
            m=max(m,nums[i])
            maxi[i]=m

        mi=float("inf")
        for i in range(n-1,-1,-1):
            mi=min(mi,nums[i])
            mini[i]=mi
        
        
        idx=-1
        for i in range(n):
            score=maxi[i]-mini[i]
            if score<=k :
                return i
        return idx
        
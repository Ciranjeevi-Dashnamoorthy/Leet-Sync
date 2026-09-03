class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        from collections import Counter
        n=len(nums)
        dp=[float("inf")]*n
        
        for i in range(n):
            d=Counter()
            ct=0
            for j in range(i,-1,-1):
                d[nums[j]]+=1
                if d[nums[j]]==2:
                    ct+=2
                elif d[nums[j]]>2:
                    ct+=1
                prev=dp[j-1] if j>0 else 0
                dp[i]=min(dp[i],prev+ct+k)
           
        return dp[-1]




        
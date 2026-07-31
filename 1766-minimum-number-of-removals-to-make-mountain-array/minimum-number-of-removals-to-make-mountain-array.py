class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[j]+1,dp[i])
        
        
        dp1=[1]*n
        nums1=nums[::-1]
        for i in range(n):
            for j in range(i):
                if nums1[j]<nums1[i]:
                    dp1[i]=max(dp1[j]+1,dp1[i])
        dp1=dp1[::-1]
        s=0
        for i in range(1,n-1):
            if dp[i]>1 and dp1[i]>1:
             curr=dp[i]+dp1[i]-1
             s=max(curr,s)
        print(dp)
        print(dp1)
        print(s)

        if s<=2:
            return n
        else:
            return n-s        
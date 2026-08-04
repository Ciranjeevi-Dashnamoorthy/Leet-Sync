class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        """
        Stndard lis with count array
        c[i] represents the number of LIS ends with ith element

        then how do we initiate the first one and count the already existing ones ??

        """

        n=len(nums)

        dp=[1]*n
        count=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    count[i]=count[j]

                elif nums[j]<nums[i] and dp[j]+1==dp[i]:
                    dp[i]=dp[j]+1
                    count[i]+=count[j]
                    
               
      

        maxi=max(dp)
        ans=0
        for i in range(n):
            if maxi==dp[i]:
                ans+=count[i]
        return ans
        
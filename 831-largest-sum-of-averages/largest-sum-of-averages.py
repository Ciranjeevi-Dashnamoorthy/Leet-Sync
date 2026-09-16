class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        """
        
        
        """

        n=len(nums)
        pref=[0]*(n+1)

        for i in range(1,n+1):
            pref[i]=pref[i-1]+nums[i-1]
        
        @cache
        def dp(idx,rem):
            if idx==n or rem==0:
                return 0
            if rem==1:
                return (pref[n]-pref[idx])/(n-idx)

            ans=0
            for i in range(idx+1,n-rem+2):
                avg=(pref[i]-pref[idx])/(i-idx)
                ans=max(ans,avg+dp(i,rem-1))
            return ans
            
        

        return dp(0,k)
        
        
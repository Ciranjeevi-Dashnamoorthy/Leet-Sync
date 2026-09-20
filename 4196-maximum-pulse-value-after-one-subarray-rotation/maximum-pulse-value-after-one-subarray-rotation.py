class Solution:
    def maxValue(self, nums: List[int]) -> int:

        """
        create an array to recored the delta 
        cretae prefix sum of it

        when we choose l and r of even lenghted subarray 
        choosing odd ones doesnt contribute
        """

        n=len(nums)
        pref=[0]*(n+1)
        for i in range(1,n+1):
            
            if i%2==1:
                pref[i]=pref[i-1]+nums[i-1]
            else:
                pref[i]=pref[i-1]-nums[i-1]
        
        maxi_even=0
        maxi_odd=float("-inf")
        
        mini=float("inf")

        for i in range(1,n+1):

            if i%2==0:
                mini=min(mini,pref[i]-maxi_even)
                maxi_even=max(maxi_even,pref[i])
            else:
                if maxi_odd!=float("inf"):
                    mini=min(mini,pref[i]-maxi_odd)
                maxi_odd=max(maxi_odd,pref[i])
        
        return pref[-1]-2*min(mini,0)

        
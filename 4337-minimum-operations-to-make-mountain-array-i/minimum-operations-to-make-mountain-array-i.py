class Solution:
    def minOperations(self, nums: list[int]) -> int:

        n=len(nums)
        if n<3:
            return -1
        maxi=max(nums)+n-1
        pref=[[float("inf")]*(maxi+1) for _ in range(n)]
        mini=float("inf")
        for i in range(1,maxi+1):
            cost=abs(nums[0]-i)
            mini=min(mini,cost)
            pref[0][i]=mini
            
        
        for i in range(1,n):
            curr=float("inf")
            for j in range(i+1,maxi+1):
                cost=abs(nums[i]-j)+pref[i-1][j-1]
                curr=min(curr,cost)
                pref[i][j]=curr 
        
        suff=[[float("inf")]*(maxi+1) for _ in range(n)]
        mini=float("inf")
        for i in range(1,maxi+1):
            cost=abs(nums[-1]-i)
            mini=min(mini,cost)
            suff[-1][i]=mini
            
        
        for i in range(n-2,-1,-1):
            curr=float("inf")
            min_len=n-i
            for j in range(min_len,maxi+1):
                cost=abs(nums[i]-j)+suff[i+1][j-1]
                curr=min(curr,cost)
                suff[i][j]=curr 
        
        ans=float("inf")

        for i in range(1,n-1):
            min_peak=max(i+1,n-i)
            for j in range(min_peak,maxi+1):
                cost=pref[i-1][j-1]+suff[i+1][j-1]+abs(nums[i]-j)
                ans=min(ans,cost)
        return ans 


        




                
                
                
            
        
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        pref=[0]*(n+1)
        from collections import defaultdict

        left=defaultdict(int)
        right=defaultdict(int)

        for i in range(1,n+1):
            pref[i]=pref[i-1]+nums[i-1]
        ct=0
        for i in range(2,n+1):
            l=pref[i-1]
            r=pref[-1]-pref[i-1]
            req=l-r
            right[req]+=1
            if l==r:
                ct+=1
            
        
        for i in range(n):
            change=k-nums[i]
            curr=left[change]+right[-change]
            ct=max(curr,ct)
            
            if i<n-1:
                l=pref[i+1]
                r=pref[-1]-pref[i+1]
                req=l-r
                right[req]-=1
                left[req]+=1

        return ct

        
            
        
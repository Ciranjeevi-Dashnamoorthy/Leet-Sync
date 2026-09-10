class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n=len(stones)
        pref=[0]*(n+1)

        total=n
        while total>1:
            curr=total%k + total//k
            
            if total==curr:
                return -1
            total=curr
        

        for i in range(1,n+1):
            pref[i]=pref[i-1]+stones[i-1]
        
        @cache
        def dp(l,r):

            if l==r:
                return 0
            
            ans=float("inf")
            for i in range(l,r,k-1):
                ans=min(ans,dp(l,i)+dp(i+1,r))
            
            if (r-l)%(k-1)==0:
                ans+=pref[r+1]-pref[l]

            return ans
        
        return dp(0,n-1)

        
        
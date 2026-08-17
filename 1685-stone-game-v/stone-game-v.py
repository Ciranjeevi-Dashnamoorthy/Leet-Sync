class Solution:
    def stoneGameV(self, nums: List[int]) -> int:

        n=len(nums)
        pref=[0]*(n+1)

        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        
        memo=[[-1]*n for _ in range(n)]
        def dp(l,r):

            if l==r:
                return 0
            if memo[l][r]!=-1:
                return memo[l][r]
            
            res=0
            for i in range(l,r):
                left=pref[i+1]-pref[l]
                right=pref[r+1]-pref[i+1]

                if left<right:
                    res=max(res,left+dp(l,i))
                elif left==right:
                   res=max(res,left+dp(l,i),right+dp(i+1,r))
                else:
                     res =max(res,right+dp(i+1,r))
            memo[l][r]=res
            return res
            

        


        return dp(0,n-1)
        
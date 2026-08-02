class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        
        
        s=sum(nums)
        n=len(nums)
        target=s//2

        dp=[[False]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=True
        
        for i in range(1,n+1):
            curr=nums[i-1]
            for j in range(1,target+1):

                dp[i][j]=dp[i-1][j]

                if j>=curr:
                    noskip=dp[i-1][j-curr]
                    dp[i][j]=noskip or dp[i][j]
        
        for i in range(target,-1,-1):
            if dp[n][i]:

                return (s-i)-i
        return 0
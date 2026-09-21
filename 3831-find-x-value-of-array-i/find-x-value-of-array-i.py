class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        n=len(nums)

        dp=[[0]*k for _ in range(n)]

        for i in range(n):
            dp[i][nums[i]%k]+=1

            if i==0:
                continue
            else:
                for r  in range(k):
                    dp[i][(r*nums[i])%k]+=dp[i-1][r]
        
        res=[0]*k
        for r in range(k):
            ct=0
            for i in range(n):
                ct+=dp[i][r]
            res[r]+=ct
        return res



        
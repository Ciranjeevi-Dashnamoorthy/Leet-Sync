class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        removing pref and suff points reduces to choosing contigous subarrays 
        and tracking the contribution that subarray provides to the value x

        define dp[i][k] where i index and k is the rem

        for every values ending eith nums[i] track its new rem

        if prev index leaves value like 1, 2
        what are the new values can be obtained by adding nums[i] to it 
        we can multiply nums[i] tp the remainders of the prev index and sdd their contribution

        """

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



        
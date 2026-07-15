class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        """
        use of inetrval dp

        for a specific interval i and j

        pick a balloon k to be burst at last

        derive the recurrence relation as follows

        dp[i][j]= max(dp[i][j], arr[i]*arr[k]*arr[j] + dp[i][k] + dp[k][j])

        dp[i][j] --> how many max poss coins we get from destroying all the baloons in 
                     the range i to j

        """

       
        nums.insert(0,1)
        nums.append(1)
        n=len(nums)
        
        dp=[[0]*(n) for _ in range(n)]

        for l in range(3,n+1):
            for i in range(n-l+1):
                j=i+l-1

                for k in range(i+1,j):
                   

                    total=nums[i]*nums[k]*nums[j]+dp[i][k]+dp[k][j]

                    dp[i][j]=max(total,dp[i][j])

        return dp[0][n-1]


        
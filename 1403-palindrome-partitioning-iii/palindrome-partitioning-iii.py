class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        Observation

        build for every partition upto k , store 
        use them for k+1 th partition

        Use Partition DP , in general minimize the problem 
        to core of what they need

        in this one they need minimal changes so we go to some index i
        for kth partion what is the minimum changes 
        so how do we get that 
        precompute the chnges required to make the partiton into plaindrome and 
        minimize the cahnges

        for example for index 5
        we have to build  2 partition
        in this two prtition the cost is what 
        the cost making this 0 to j , j+1 to i 
        into palindrome 

        """

        n=len(s)
        cost=[[0]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):

                if s[i]==s[j]:
                    cost[i][j]=cost[i+1][j-1]
                else:
                    cost[i][j]=cost[i+1][j-1]+1

    
        
        dp=[[float("inf")]*(k+1) for _ in range(n+1)]
        dp[0][0]=0
        for i in range(1,n+1):
             for j in range(1,k+1):

                if j>i:
                    break
                
                for p in range(j-1,i):

                    dp[i][j]=min(dp[i][j],dp[p][j-1]+cost[p][i-1])
        
        return dp[n][k]
                
                
           
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)

        dp=[[float("-inf")]*2 for _ in range(n)]
       
        def check(idx,buy):

            if idx>=n:
                return 0

            if dp[idx][buy]!=float("-inf"):
                return dp[idx][buy]
            print(idx,buy)
            
            if buy==1:
                skip=check(idx+1,buy)
                bought=-prices[idx]+check(idx+1,0)
                dp[idx][buy]=max(skip,bought)
            
            else:
                skip=check(idx+1,buy)
                sell=prices[idx]+check(idx+2,1)
                dp[idx][buy]=max(skip,sell)
            
            return dp[idx][buy]
        
        check(0,1)
        print(dp)
        return dp[0][1]
        
            
        
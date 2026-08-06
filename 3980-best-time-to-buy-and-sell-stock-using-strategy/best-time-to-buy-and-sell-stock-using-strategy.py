class Solution:
    def maxProfit(self, prices: List[int], nums: List[int], k: int) -> int:

        """
    
        Sliding window with minimum doesnt work 

        window with best profit doesnt work

        window with best delta for profits works , how to implemnent it
        precompute the buy and sell
        precompute prices arrays to check for modification delta increase in profit

        Greedy choosing doesnt work explaore all windows..
        """

        n=len(prices)

        pref=[0]*(n+1)
        pri=[0]*(n+1)

        for i in range(n):
            pref[i+1]= pref[i]+nums[i]*prices[i]
            pri[i+1]=pri[i]+prices[i]
        maxi=pref[-1]
        delta=0

        for i in range(n-k+1):
            curr=pref[i+k]-pref[i]
            
            new=pri[i+k]-pri[i+k//2]

            if new-curr>delta:
                delta=new-curr

        return maxi+delta
        
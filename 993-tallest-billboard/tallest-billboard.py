class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        n=len(rods)
       
        @cache
        def dp(idx,diff):
            if idx==len(rods):
                if diff==0:
                    return 0
                else:
                    return float("-inf")
            
            skip=dp(idx+1,diff)
            take1=rods[idx]+dp(idx+1,diff+rods[idx])
            take2=dp(idx+1,diff-rods[idx])

            maxi=max(skip,take1,take2)
            return maxi
   
        
        return dp(0,0)
        
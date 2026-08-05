class Solution:
    def canIWin(self, n: int, target: int) -> bool:

        """
        DP(bit,current_val)
        bit-> holds which numbers already choosen
        current_val -> holds the rem amount to win

        """
        @cache
        def dp(bit,total):
            for i in range(1,n+1):
             if bit & (1 << i) == 0:
                if i>=total:
                    return True
                
                new=bit|(1 << i)
                if not dp(new,total-i):
                    return True
                
            return False
        
        if (n*(n+1))//2 < target:
            return False

        fl=dp(0,target)
        return fl


        
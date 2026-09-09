class Solution:
    def countCommas(self, n: int) -> int:
        """
        highest 
        
        1,000,000,000,000,000 - 15 zeros

        ex

        9,843,839 = n

        comma= n - 999,999
        new n = 999,999

        comma+=n-999


        """
        
        ans=max(n-999,0)+max(0,n-999999)+max(0,n-999999999)+max(0,n-999999999999)+max(n-999999999999999,0)


        return ans

        
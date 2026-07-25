class Solution:
    def maxProduct(self, n: int) -> int:
        fir,sec=0,0
        
        while n>0:
            curr=n%10
            if curr>fir:
                sec=fir
                fir=curr
            else:
                sec=max(sec,curr)
            n//=10
          
        return fir*sec

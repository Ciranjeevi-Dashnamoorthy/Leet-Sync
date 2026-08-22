class Solution:
    def checkDivisibility(self, n: int) -> bool:

        s=0
        p=1
     
        for num in str(n):
            s+=int(num)
            p*=int(num)
            

        return n%(s+p)==0
        
        
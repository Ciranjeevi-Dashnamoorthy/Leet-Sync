class Solution:
    def minChanges(self, s: str) -> int:

        n=len(s)
        zero=0
        one=0
        change=0

        for i in range(n):
            if s[i]=="0":
                zero+=1
                if one%2==1:
                    change+=1
                    zero-=1
                one=0

            else:
                one+=1
                if zero%2==1:
                    change+=1
                    one-=1
                zero=0
        return change
            
            
        
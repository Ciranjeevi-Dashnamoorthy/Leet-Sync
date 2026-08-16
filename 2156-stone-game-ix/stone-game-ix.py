class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        zero,one,two=0,0,0

        for s in stones:
            rem=s%3
            if rem==0:
                zero+=1
            elif rem==1:
                one+=1
            else:
                two+=1
        
        if zero%2==0:
            if one>0 and two>0:
                return True
            else:
                return False
        
        if abs(one-two)>2:
            return True
        else:
            return False
        
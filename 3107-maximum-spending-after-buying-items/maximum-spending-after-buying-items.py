class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:

        m,n=len(values),len(values[0])
        ans=0
        d=1
        last=[n-1]*m
        total=m*n
        while total!=0:
            mini=float("inf")
            pos=0
            for j in range(m):
                idx=last[j]
                if idx>=0 and values[j][idx]<mini:
                    pos=j
                    mini=values[j][idx]
           
            ans+=(d*mini)
            last[pos]-=1
            d+=1
            total-=1
         
        return ans
        



        
from functools import cache
from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:

        """
        masking to represent the course taken or not

        """
        from collections import defaultdict
        
        pre=[0]*n

        for u,v in relations:
            u-=1
            v-=1
            new=1<<u
            pre[v]|=new 
        target=(1<<n) -1

        @cache
        def back(mask):

            if mask == target:
                return 0 
            
            avai=[]
            for i in range(n):
                if (mask& (1<<i))==0 and (mask & pre[i])==pre[i]:
                    avai.append(i)
            
            if len(avai)<=k:
                new=mask 
                for c in avai:
                    new|=(1<<c)
                ans=1+back(new)
                return ans 
            ans=float("inf")
            for comb in combinations(avai,k):
                new=mask 
                for c in comb:
                    new|=(1<<c) 
                ans=min(ans,1+back(new))
            return ans 

        return back(0)
        
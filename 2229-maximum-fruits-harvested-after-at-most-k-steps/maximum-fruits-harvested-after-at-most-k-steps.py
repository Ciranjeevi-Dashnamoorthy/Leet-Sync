class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], st: int, k: int) -> int:

        n=len(fruits)
    
        from collections import defaultdict
        d=defaultdict(int)
        for pos,v in fruits:
            d[pos]=v

        s=max(0,st-k)
        curr=0

        for i in range(s,st+1):
            if i in d:
                curr+=d[i]
        
        
        l=st-k
        steps=k//2
        ans=curr
        for r in range(st+1,steps+st+1):
            
            
            curr+=d[r]
            curr-=d[l]
            curr-=d[l+1]
            l+=2
            ans=max(ans,curr)
       
        curr=0
        for i in range(st,st+k+1):
            if i in d:
                curr+=d[i]
        
        
        r=st+k
        steps=k//2
        ans=max(ans,curr)
        s=st-steps
        
        for l in range(st-1,s-1,-1):
            
            
            curr+=d[l]
            curr-=d[r]
            curr-=d[r-1]
            r-=2
            ans=max(ans,curr)
       
        return ans



        
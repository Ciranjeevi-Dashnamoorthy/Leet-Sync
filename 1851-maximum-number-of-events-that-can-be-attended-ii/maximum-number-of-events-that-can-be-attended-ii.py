class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        idx={}
        ct=0
        for s,e,v in events:
            if (s,e,v) not in idx:
                idx[(s,e,v)]=ct
            ct+=1
        events=sorted(idx)
        n=len(events)

        @cache
        def dp(i,k):
            if i==n or k==0:
                return 0 
            
            skip=dp(i+1,k)
            s,e,v=events[i]
            nexti=bisect.bisect_left(events,(e+1,))
            take=v+dp(nexti,k-1)

            return max(skip,take)
        return dp(0,k)

            
            
    

import bisect
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        """
        Observation:
        0-1 knapsack 
        mainatin extra state for pickinh limit upto 4 
        and get the max poss score for it

        how do we condition the non - overlapping 
        use binary derach to find the next suitbale index
        
        """

        idx={}
        ct=0
        for l,r,w in intervals:
            if (l,r,w) not in idx:
                idx[(l,r,w)]=ct
            ct+=1
        intervals=sorted(idx)
        n=len(intervals)
       

        @cache
        def dp(i,rem):

            if i==n or rem==0:
                return 0,[]
            
            skipw,skipind=dp(i+1,rem)
            l,r,w=intervals[i]
            nexti=bisect.bisect_left(intervals,(r+1,))

            nextw,nextind=dp(nexti,rem-1)
            takew=nextw+w
            takeind=nextind+[idx[(l,r,w)]]
            takeind.sort()

            if skipw>takew:
                return (skipw,skipind)
            elif skipw<takew:
                return (takew,takeind)
            if skipind<takeind:
                return (skipw,skipind)
            else:
                return (takew,takeind)
        ans=dp(0,4)
        return ans[1]



        
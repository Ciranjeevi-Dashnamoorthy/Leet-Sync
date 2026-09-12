import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        d={}
        for i in range(len(profit)):
            s,e,p=startTime[i],endTime[i],profit[i]
            if (s,e) not in d:
                d[(s,e)]=i
            else:
                prev=d[(s,e)]
                if profit[prev]<profit[i]:
                    d[(s,e)]=i
        check=sorted(d)
        n=len(check)
        print(check)

        @cache
        def dp(idx):
            if idx==n:
                return 0
            skip=dp(idx+1)
            s,e=check[idx]
            idx1=d[(s,e)]
            nexti=bisect.bisect_left(check,(e,))
            take=profit[idx1]+dp(nexti)
            return max(take,skip)
        return dp(0)

        
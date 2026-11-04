from sortedcontainers import SortedList
from collections import defaultdict
import heapq
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        
        n=len(nums)
        upper=[]
        lower=[]
        cost=[]
        usum=0
        lsum=0
        lsize=0
        usize=0
        updel=defaultdict(int)
        lowdel=defaultdict(int)

        def balance():
            nonlocal lsum, usum, lsize, usize
            
           
            while lsize < usize:
                while upper and updel[upper[0]] > 0:
                    updel[upper[0]] -= 1
                    heapq.heappop(upper)
                val = heapq.heappop(upper)
                usum -= val
                usize -= 1
                heapq.heappush(lower, -val)
                lsum += val
                lsize += 1
                
            
            while lsize - usize > 1:
                while lower and lowdel[-lower[0]] > 0:
                    lowdel[-lower[0]] -= 1
                    heapq.heappop(lower)
                val = -heapq.heappop(lower)
                lsum -= val
                lsize -= 1
                heapq.heappush(upper, val)
                usum += val
                usize += 1
                

            while lower and lowdel[-lower[0]] > 0:
                lowdel[-lower[0]] -= 1
                heapq.heappop(lower)
            while upper and updel[upper[0]] > 0:
                updel[upper[0]] -= 1
                heapq.heappop(upper)

        for i in range(n):
            if not lower or nums[i]<=-lower[0]:
                lsum+=nums[i]
                heapq.heappush(lower,-nums[i])
                lsize+=1
            else:
                usum+=nums[i]
                heapq.heappush(upper,nums[i])
                usize+=1
            
            if i>=x:
                out=nums[i-x]
                if upper and out>=upper[0]:
                    updel[out]+=1
                    usize-=1
                    usum-=out
                else:
                    lsum-=out
                    lowdel[out]+=1
                    lsize-=1
            balance()

            if i>=x-1:
                median=-lower[0]
                val=(median*lsize-lsum)+(usum-median*usize)
                cost.append(val)


        dp=[0]*(n+1)

        for rem in range(1,k+1):
            next_dp=[float("inf")]*(n+1)
            for i in range(n-rem*x,-1,-1):
                skip=next_dp[i+1]
                noskip=cost[i]+dp[i+x]
                next_dp[i]=min(skip,noskip)
            dp=next_dp
        return dp[0]







    


        
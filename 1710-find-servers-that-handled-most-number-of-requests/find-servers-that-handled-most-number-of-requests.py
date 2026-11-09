import heapq
import bisect
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        n=len(arrival)
        free=[]
        busy=[]
        
        ans=[0]*(k)
        for i in range(k):
            heapq.heappush(free,(i))
            
        currid=k+1
        for i in range(n):
            time=arrival[i]
            
            while busy and busy[0][0]<=time:
                    end,prev=heapq.heappop(busy)
                    heapq.heappush(free,prev)
                
            while free and free[0]<i:
                idx=heapq.heappop(free)
                heapq.heappush(free,idx+k)
                
            
            if free:
                idx=heapq.heappop(free)
                
                ans[(idx)%k]+=1
                heapq.heappush(busy,(time+load[i],idx))
            
            
            
        maxi=max(ans)
        final=[]
        for i in range(k):
            if ans[i]==maxi:
                final.append(i)
        return final
            


        
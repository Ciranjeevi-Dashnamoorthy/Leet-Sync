import heapq
from collections import defaultdict
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:

        """
        two heap - minheap and maxheap 
        for lower and gretr half

        """

        small=[]
        large=[]
        n=len(nums)
        for i in range(k):
            heapq.heappush(small,-nums[i])
        for  _ in range((k)//2):
            heapq.heappush(large,-heappop(small))
        def median():
            if k%2==1:
                return float(-small[0])
            return (-small[0]+large[0])/2.0
        ans=[median()]
        
        delayed=defaultdict(int)
        for i in range(k,n):
            out=nums[i-k]
            inp=nums[i]
            delayed[out]+=1

            if out<=-small[0]:
                balance=1
            else:
                balance=-1

            if inp<=-small[0]:
                balance-=1
                heapq.heappush(small,-nums[i])
            else:
                balance+=1
                heapq.heappush(large,nums[i])
            
            if balance<0:
                heapq.heappush(large,-heapq.heappop(small))
            elif balance>0:
                heapq.heappush(small,-heapq.heappop(large))
            
            while small and delayed[-small[0]]>0:
                delayed[-small[0]]-=1
                heapq.heappop(small)
                
            while large and delayed[large[0]]>0:
                delayed[large[0]]-=1
                heapq.heappop(large)
                
            
            ans.append(median())
        return ans 
            
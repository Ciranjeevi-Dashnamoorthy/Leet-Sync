import heapq
class Solution:
    def maximumRobots(self, charge: list[int], run: list[int], budget: int) -> int:

        n=len(charge)
        curr=0
        l=0
        heap=[]
        maxi=0
        for r in range(n):
            curr+=run[r]
            heapq.heappush(heap,(-charge[r],r))
            
            while heap and (-heap[0][0]+ (r-l+1)*(curr)>budget):
                curr-=run[l]
                l+=1
                while heap and heap[0][1]<l:
                    heapq.heappop(heap)
            if heap:
                total=-heap[0][0]+ (r-l+1)*(curr)
                if total<=budget:
                    maxi=max(maxi,r-l+1)
        return maxi


        
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        import heapq

        heap=[]
        poss=[]
        n=len(wage)
        for i in range(n):
            poss.append((wage[i]/quality[i],i))
        poss.sort()
        
        heap=[]
        curr=0
        
        for i in range(k):
            val,idx=poss[i]
            curr+=quality[idx]
            heappush(heap,-quality[idx])
        
        ans=curr*poss[k-1][0]
        
        for i in range(k,n):
            val,idx=poss[i]
            curr+=quality[idx]
            heappush(heap,-quality[idx])
            curr-=-heappop(heap)
            ans=min(ans,curr*val)
        return ans

        
        
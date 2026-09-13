class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        import heapq
        heap=[]
        poss=[]
        mod=10**9 + 7
        for i in range(n):
            poss.append((efficiency[i],i))
        poss.sort(reverse=True)
        curr=0
        ans=0
        for i in range(k):
            val,idx=poss[i]
            curr=(curr+speed[idx])
            heappush(heap,speed[idx])
            ans=max((curr*val),ans)
        for i in range(k,n):
            val,idx=poss[i]
            curr=(curr+speed[idx])
            heappush(heap,speed[idx])
            curr-=heappop(heap)
            ans=max(ans,(curr*val))

        return ans%mod


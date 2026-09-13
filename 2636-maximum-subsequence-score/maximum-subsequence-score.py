class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq

        heap=[]
        poss=[]
        n=len(nums1)
        for i in range(n):
            poss.append((nums2[i],i))
        poss.sort(reverse=True)
        
        heap=[]
        curr=0
        for i in range(k):
            val,idx=poss[i]
            curr+=nums1[idx]
            heapq.heappush(heap,nums1[idx])
        
        ans=curr*poss[k-1][0]
        
        for i in range(k,n):
            val,idx=poss[i]
            curr+=nums1[idx]
            heapq.heappush(heap,nums1[idx])
            curr-=heapq.heappop(heap)
            ans=max(ans,curr*poss[i][0])
        return ans
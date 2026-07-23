class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], need: int, limit: int) -> int:
        import heapq
        from collections import defaultdict

        heap=[]
        n=len(values)
        for i in range(n):
            heapq.heappush(heap,(-values[i],labels[i]))
        
        d=defaultdict(int)
        ans=0
        
        while heap and need>0:
            val,lab=heapq.heappop(heap)
            if d[lab]<limit:
                d[lab]+=1
                ans+=-val
                need-=1
            print(ans)
        return ans
            

        
        
        
        
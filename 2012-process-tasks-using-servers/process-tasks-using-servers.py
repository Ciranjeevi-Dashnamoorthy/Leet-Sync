class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        """
        """
        
        import heapq
        from collections import defaultdict

        busy=[]
        free=[]
        for i in range(len(servers)):
            heapq.heappush(free,(servers[i],i))
        t=0
        ans=[]
        for i in range(len(tasks)):
            t=max(t,i)

            if not free:
                t=max(t,busy[0][0])
            
            while busy and busy[0][0]<=t:
                _,w,idx=heapq.heappop(busy)
                heapq.heappush(free,(w,idx))
            
            wei,idx=heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy,(t+tasks[i],wei,idx))
        return ans




        

        
        
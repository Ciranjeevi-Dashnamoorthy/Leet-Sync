class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        
        adj=[[] for _ in range(n+1)]
        indegree=[0]*(n+1)
        for u,v in relations:
            adj[u].append(v)
            indegree[v]+=1
        
        queue=deque([])
        for i in range(1,n+1):
            if indegree[i]==0:
                queue.append((i,time[i-1]))
        maxi=max(time)
        base=time[::]
        while queue:
            node,t=queue.popleft()
            for nei in adj[node]:
                indegree[nei]-=1
                base[nei-1]=max(base[nei-1],t+time[nei-1])
                maxi=max(maxi,base[nei-1])
                if indegree[nei]==0:
                    queue.append((nei,base[nei-1]))
        return maxi



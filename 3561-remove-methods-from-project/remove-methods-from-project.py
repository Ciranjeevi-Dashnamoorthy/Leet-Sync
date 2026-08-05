class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        """
        Standard BFS
        if a non -inf method touches a infec method then all the method can be invoked
        else return only the healthy ones
        """
        
        adj=[[] for _ in range(n)]
        from collections import deque


        for u,v in invocations:

            adj[u].append(v)
        
        queue=deque([k])
        inf=set()
        inf.add(k)

        while queue:
            node=queue.popleft()

            for nei in adj[node]:
                if nei not in inf:
                    inf.add(nei)
                    queue.append(nei)

       
        for u in range(n):
            fl=False
            if u not in inf:
                for v in adj[u]:
                    if v in inf:
                        fl=True
                        break
            if fl:
                break
        res=[]
        if fl:
            return list(range(n))
        else:
            for i in range(n):
                if i not in inf:
                    res.append(i)
            return res
            


        
        

        
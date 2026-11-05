class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:

        n=len(nums)
        s=sum(nums)
        div=[]
        adj=[[] for _ in range(n)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        maxi=0
        def find(k):
            vis=set()
            self.ct=0
            def dfs(node):
           
                vis.add(node)
                val=nums[node]

                for nei in adj[node]:
                    if nei not in vis: 
                        val+=dfs(nei)
                if val==k:
                    self.ct+=1
                    return 0
                return val
            if dfs(0)==0:
                return self.ct-1
            else:
                return 0
                
        
        
        for i in range(max(nums),s//2+1):
            if s%i==0:
                val=find(i)
                if val!=0:
                    return val
        return 0
                    
        
                

        
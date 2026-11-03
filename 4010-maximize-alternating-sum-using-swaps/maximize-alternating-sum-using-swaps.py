class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) :
        m=len(nums)
        adj=[[] for _ in range(m)]
        start=-1
        arr=set()
        for u,v in swaps:
            adj[u].append(v)
            adj[v].append(u)
            arr.add(u)
            arr.add(v)
        arr=list(arr)
        vis=set()
        n=len(arr)
        def dfs(node):
            vis.add(node)
            group.append(node)
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)
        groups=[] 
        print(arr)
        for i in range(n):
            node=arr[i]
            group=[]
        
            if node not in vis:
                dfs(node)
            if group:
                groups.append(group)
        cost=[]
        for group in groups:
            cost=[]
            even=0
            odd=0
            for idx in group:
                cost.append((nums[idx],idx))
                if idx%2==0:
                    even+=1
                else:
                    odd+=1
            cost.sort(reverse=True)
            i=0
            for idx in group:
                if idx%2==0:
                    nums[idx]=cost[i][0]
                    i+=1
            for idx in group:
                if idx%2==1:
                    nums[idx]=cost[i][0]
                    i+=1
        val=0
      
        for i in range(len(nums)):
            if i%2==0:
                val+=nums[i]
            else:
                val-=nums[i]
           
        return val


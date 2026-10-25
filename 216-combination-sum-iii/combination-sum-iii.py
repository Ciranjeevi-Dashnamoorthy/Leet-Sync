class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        nums=[]
        ans=[]
        for i in range(1,10):
            nums.append(i)
        
        def dfs(idx,path,curr):
            if len(path)==k and curr==n:
                ans.append(path[::])
                return
            if len(path)>k:
                return 
            
            for i in range(idx,9):
                if curr+nums[i]>n:
                    return
                path.append(nums[i])
                dfs(i+1,path,curr+nums[i])
                path.pop()
            
        dfs(0,[],0)
        return ans    
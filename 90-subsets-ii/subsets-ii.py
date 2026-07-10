class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()
        n=len(nums)

        def dfs(start,path):
            
            res.append(path[::])
            
            for i in range(start,n):
                if i>start and nums[i-1]==nums[i]:
                    continue
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
               
        dfs(0,[])
        return res
                
        

        
        dfs(0,[])
        return res
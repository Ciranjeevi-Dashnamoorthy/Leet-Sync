class Solution:
    def canSeePersonsCount(self, nums: list[int]) -> list[int]:

        n=len(nums)
        stack=[]
        res=[0]*n
        
        for i in range(n-1,-1,-1):
            
            while stack and stack[-1]<nums[i]:
                stack.pop()
                res[i]+=1
            if stack:
                res[i]+=1
            stack.append(nums[i])
            
            
        return res

        
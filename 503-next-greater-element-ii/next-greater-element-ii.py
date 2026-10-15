class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        n=len(nums)

        stack=[]
        res=[-1]*n 

        for idx in range(2*n):
            i=idx%n

            while stack and nums[stack[-1]]<nums[i]:
                new=stack.pop()
                res[new]=nums[i]
            
            if idx<n:
                stack.append(idx)
        
        return res
        
class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:

        n=len(nums)

        left=[-1]*n
        right=[n]*n
        stack=[]
        for i in range(n):
            while stack and (nums[i]|nums[stack[-1]])==nums[i] and nums[i]!=nums[stack[-1]]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and (nums[i]|nums[stack[-1]])==nums[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)
        ans=0
        for i in range(n):
            ans+=(i-left[i])*(right[i]-i)
        return ans


        
        

                
        
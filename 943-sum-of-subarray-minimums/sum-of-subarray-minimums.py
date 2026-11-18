class Solution:
    def sumSubarrayMins(self, nums: list[int]) -> int:

        stack=[(0,-1)]
        n=len(nums)
        ans=0
        mod=10**9 + 7
    
        for i in range(n):
            right=i
            while stack and stack[-1][0]>=nums[i]:

                val,mid=stack.pop()
                left=stack[-1][1]
            
                ans=(ans+(val*(mid-left)*(right-mid)))%mod
            
            stack.append((nums[i],i))
        
        while len(stack)>1:
            val,mid=stack.pop()
            left=stack[-1][1]
            ans=(ans+(val*(mid-left)*(n-mid)))%mod
        return ans 
        
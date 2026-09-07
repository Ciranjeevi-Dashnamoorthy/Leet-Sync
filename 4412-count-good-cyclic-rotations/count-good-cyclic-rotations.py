class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:

        n=len(nums)
        firs,sec=0,0
        for i in range(n):
            if i<n//2:
                firs+=nums[i]
            else:
                sec+=nums[i]
        ct=0
      
        mid=n//2

        for i in range(n):
            sec-=nums[n-1-i]
            firs+=nums[n-1-i]
         
            
            firs-=nums[(mid-i-1)%n]
            sec+=nums[(mid-1-i)%n]
           
        
            if firs>sec:
                ct+=1
        return ct
            
        
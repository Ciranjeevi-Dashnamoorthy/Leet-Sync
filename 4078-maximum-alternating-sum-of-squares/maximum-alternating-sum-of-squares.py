class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        score=0
        l,r=0,len(nums)-1
        
        while l<r:
            
            score+=nums[r]
            
            score-=nums[l]
            
            l+=1
            r-=1
        if len(nums)%2!=0:
            score+=nums[l]
            
        return score
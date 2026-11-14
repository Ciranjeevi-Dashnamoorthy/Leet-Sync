class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:

        n=len(nums)
        nums1=nums[::]
        ops1=0
        for i in range(n-1):
            if nums1[i]>nums1[i+1]:
                nums1[i+1]=nums1[i]
                ops1+=1
        
        
        ops2=0
        for i in range(n-1,0,-1):
            if nums[i]<nums[i-1]:
                nums[i-1]=nums[i]
                ops2+=1
            if i<n-1:
                if nums[i]>nums[i+1]:
                    ops2+=1
        
        if ops1<=1 or ops2<=1:
            return True 
        else:
            return False


            

        
class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:

        n=len(nums)
        nums1=nums[::]
        op1=0
        for i in range(n-1):
            if nums1[i]>nums1[i+1]:
                nums1[i]=nums1[i+1]
                op1+=1
        print(op1)
        print(nums)
        fl=True
        for i in range(n-1):
            if nums1[i]>nums1[i+1]:
                fl=False
                break 
        if fl and op1<=1:
            return True
        fl=True 
        op2=0
        for i in range(n-1,-0,-1):
            if nums[i]<nums[i-1]:
                nums[i]=nums[i-1]
                op2+=1
        
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                fl=False 
                break 
        if fl and op2<=1:
            return  True 
        return False


        
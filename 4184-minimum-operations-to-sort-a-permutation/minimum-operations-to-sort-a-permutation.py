class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n=len(nums)
        inc=1
        dec=1

        for i in range(1,n):

            if nums[i]==(nums[i-1]+1)%n:
                inc+=1
            if nums[i-1]==(nums[i]+1)%n:
                dec+=1
            
        if inc==n:
                if nums[0]!=0:
                    return min(n-nums[0],nums[0]+2)
                else:
                    return 0
        if dec==n:
                return min(n-nums[-1],nums[-1])+1
        return -1
        
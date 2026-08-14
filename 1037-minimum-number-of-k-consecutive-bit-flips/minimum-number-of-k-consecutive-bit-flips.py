class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        flip=[False]*n

        curr=0
        ops=0
        for i in range(n):

            if i>=k and flip[i-k]:
                curr-=1
            
            if (nums[i]==0 and curr%2==0) or (nums[i]==1 and curr%2==1):
                if i+k>n:
                    return -1
                ops+=1
                curr+=1
                flip[i]=True
        
        return ops

        
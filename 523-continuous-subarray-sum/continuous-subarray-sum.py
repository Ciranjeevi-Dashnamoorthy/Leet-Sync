class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        from collections import defaultdict

        d=defaultdict(int)
        d[0]=-1
        curr=0

        for i in range(n):
            curr+=nums[i]
            rem=curr%k
            
            
            if rem in d:
                if i-d[rem]>=2:
                 return True
            if rem not in d:
             d[rem]=i
             
        return False

        
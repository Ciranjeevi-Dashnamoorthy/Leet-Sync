class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        n=len(nums)
        if k==n:
            return max(nums)
        
        from collections import defaultdict
        d=defaultdict(int)
        maxi=-1
        for i in range(n-k+1):
            for j in range(i,i+k):
                d[nums[j]]+=1

        for num in d:
                if d[num]==1:
                 maxi=max(maxi,num)
        return maxi


        
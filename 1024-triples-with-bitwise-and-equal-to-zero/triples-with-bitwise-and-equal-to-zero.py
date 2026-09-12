class Solution:
    def countTriplets(self, nums: List[int]) -> int:

        from collections import defaultdict

        d=defaultdict(int)
        n=len(nums)
        for i in range(n):
            for j in range(n):
                bitand=nums[i]&nums[j]
                d[bitand]+=1
        ans=0
        for val in d:
            for i in range(n):
                if val&nums[i]==0:
                    ans+=d[val]
        return ans


        
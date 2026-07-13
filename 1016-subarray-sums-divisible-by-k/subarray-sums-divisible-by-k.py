class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        from collections import defaultdict
        d=defaultdict(int)
        d[0]=1

        n=len(nums)
        curr=0
        ans=0

        for i in range(n):
            curr+=nums[i]
            # if curr>=0:
            rem=curr%k
            # else:
            #     print(k,(-curr%k))
            #     rem=k-(-curr%k)
            # print(rem)
            ans+=d[rem]
            d[rem]+=1
        return ans      
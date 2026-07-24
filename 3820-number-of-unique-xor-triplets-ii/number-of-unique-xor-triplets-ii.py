class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        s=set()
        for i in range(n):
            for j in range(i,n):
                s.add(nums[i]^nums[j])
        res=set()
        for i in range(n):
            for v in s:
                res.add(nums[i]^v)
        return len(res)

        
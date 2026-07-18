class Solution:
    def findGCD(self, nums: List[int]) -> int:

        m,n=max(nums),min(nums)
        return gcd(n,m)
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        fl=False
        n=len(nums)
        ans=0
        for i in range(n):
            if i!=nums[i]:
                if not fl:
                    ans=nums[i]
                    fl=True
                else:
                    ans&=nums[i]
        return ans 
        
class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:

        """
        zero only comes after zero 
        one comes after zeros 
        two comes after 01 s 
        
        """

        n=len(nums)
        zero=0
        one=0
        two=0
        mod=10**9+7

        for i in range(n):
            if nums[i]==0:
                zero=(zero*2) + 1
            if nums[i]==1:
                one=(one*2)+zero
            if nums[i]==2:
                two=(two*2+one)%mod
        return two
                
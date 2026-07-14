
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        mod=10**9+7
        @cache
        def dp(idx,gcd1,gcd2):

            if idx==len(nums):
                if gcd1==gcd2:
                    return 1
                else:
                    return 0
            
            total=0
            total=(total+dp(idx+1,gcd1,gcd2))%mod
            total=(total+dp(idx+1,gcd(gcd1,nums[idx]),gcd2))%mod
            total=(total+dp(idx+1,gcd1,gcd(gcd2,nums[idx])))%mod

            return total
        
        return dp(0,0,0)-1
        
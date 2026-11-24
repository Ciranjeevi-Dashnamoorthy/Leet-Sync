
class Solution:
    def maxLength(self, nums: List[int]) -> int:

        n=len(nums)
        ans=1
        for i in range(n):
            prod=nums[i]
            gcd=nums[i]
            lcm=nums[i]
            for j in range(i+1,n):
                prod*=nums[j]
                gcd=math.gcd(nums[j],gcd)
                lcm=math.lcm(nums[j],lcm)
                if prod==lcm*gcd:
                    ans=max(j-i+1,ans)
        return ans
            
                

        
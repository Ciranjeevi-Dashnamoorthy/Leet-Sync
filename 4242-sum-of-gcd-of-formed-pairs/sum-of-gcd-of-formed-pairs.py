class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            if b==0:
                return abs(a)
            return gcd(b,a%b)
        
        m=0
        n=len(nums)
        pre=[0]*n
        for i in range(n):
            m=max(m,nums[i])
            pre[i]=gcd(nums[i],m)
        
        pre.sort()
        i,j=0,n-1
        s=0
        while i<j:
            s+=gcd(pre[i],pre[j])
            i+=1
            j-=1
        return s



        
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        from collections import defaultdict
        d=defaultdict(int)
        n=len(nums)
        base=0
        maxi=0
        for i in range(n-1):
            a,b=nums[i],nums[i+1]
            if a==b:
                base+=1
            else:
                if a>b:
                    p,q=b,a
                else:
                    p,q=a,b
                
                d[(p,q)]+=1
                if d[(p,q)]>maxi:
                    maxi=d[(p,q)]
        return base+maxi
                
        
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:

        from collections import defaultdict

        if sum(nums)<target:
            return -1

        d=defaultdict(int)

        for num in nums:
            bi=len(bin(num))-2
            d[bi-1]+=1
        
        ops=0
        for i in range(31):
            if (target>>i)&1:

                if d[i]>0:
                    d[i]-=1
                else:
                    j=i+1
                    while j<32 and d[j]==0:
                        j+=1
                    
                    d[j]-=1
                
                    for k in range(j-1,i-1,-1):
                        ops+=1
                        d[k]+=1
            d[i+1]+=d[i]//2
        return ops
                    
                

        
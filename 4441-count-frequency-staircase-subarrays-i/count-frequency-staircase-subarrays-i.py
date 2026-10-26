class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        from collections import defaultdict

        n=len(nums)
        ans=0
        for i in range(n):
            check=[False]*n
            d=defaultdict(int)
            occ=defaultdict(int)
            ct=1
            satis=0
            
            for j in range(i,n):
                val=nums[j]
                if d[val]==0:
                    d[val]=ct
                    ct+=1
                occ[val]+=1
                if occ[val]>d[val]:
                    satis-=1
                    break
                if occ[val]==d[val]:
                    satis+=1
                
                
                if satis==ct-1:
                    ans+=1
                
                    
        return ans





        
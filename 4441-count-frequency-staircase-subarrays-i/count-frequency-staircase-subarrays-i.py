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
            
            for j in range(i,n):
                val=nums[j]
                if d[val]==0:
                    d[val]=ct
                    ct+=1
                occ[d[val]]+=1
               
                fl=True
               
                for k in range(ct):
                    if occ[k]!=k:
                        fl=False
                        break
                if fl:
                    ans+=1

                    
        return ans





        
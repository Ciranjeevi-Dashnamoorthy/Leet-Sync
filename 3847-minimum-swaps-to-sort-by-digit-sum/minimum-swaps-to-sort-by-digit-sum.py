class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        from collections import defaultdict

        pos=[]
        n=len(nums)
    
        for i in range(n):
            curr=0
            for num in str(nums[i]):
                curr+=int(num)
            pos.append((curr,nums[i],i))
        pos.sort()
        steps=0

        vis=set()
        for i in range(n):
            curr=pos[i][2]
            if curr not in vis:
                s=0
                j=i
                while pos[j][2] not in vis:
                    vis.add(pos[j][2])
                    s+=1
                    j=pos[j][2]
                
                steps+=s-1
        return steps





        
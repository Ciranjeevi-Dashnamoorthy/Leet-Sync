class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        n=len(nums)
        ans=0
        for i in range(n):
            ct=0
            d={}
            dis=0
            for j in range(i,n):
                if nums[j] not in d:
                    d[nums[j]]=1
                    dis+=1
                else:
                    d[nums[j]]+=1
                    
          
                ans+=dis**2
        return ans

                

        
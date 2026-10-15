class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        n=len(nums)
        ans=0
        for i in range(n):
            s=set()
            dis=0
            for j in range(i,n):
                if nums[j] not in s:
                    s.add(nums[j])
                    dis+=1        
                ans+=dis**2
        return ans

                

        
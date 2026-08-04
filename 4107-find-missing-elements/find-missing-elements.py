class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """
        When the Random wave of sadness passes and you remember you're actually goated

        """
        nums.sort()
        s=set(nums)
        m,l=nums[0],nums[-1]
        li=[]
        for i in range(m+1,l):
            if i not in s:
                li.append(int(i))
        return li
        
        
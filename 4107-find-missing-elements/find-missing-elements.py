class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        s=set(nums)
        m,l=nums[0],nums[-1]
        li=[]
        for i in range(m,l+1):
            if i not in s:
                li.append(int(i))
        return li
        
        
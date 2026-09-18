class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        n=len(nums)

        s=set(nums)
        res=[]
        
        st=lower
        for num in range(lower,upper+1):
            
            if num in s :
                if st!=num:
                    res.append([st,num-1])
                st=num+1
            
        if st<=upper:
            res.append([st,upper])
        return res
            






class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini=min(nums)
        maxi=max(nums)
        idxi=0
        idxm=0
    

        for i in range(n):
            if nums[i]==maxi:
                idxm=i
            if nums[i]==mini:
                idxi=i

        if idxi>idxm:
            idxm,idxi=idxi,idxm
        ans=min(n-idxi,idxm+1,idxi+1+(n-idxm))
      
        return 0 if ans<0 else ans 
        
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        n=len(nums)
        prev=0
        ans=0
        
        for i in range(n):
            curr=target[i]-nums[i]

            if (curr>0 and prev>0):
                ans+=max(0,curr-prev)
            elif (curr<0 and prev<0):
                ans+=max(0,prev-curr)
            else:
                ans+=abs(curr)
            
            prev=curr 
        return ans


        
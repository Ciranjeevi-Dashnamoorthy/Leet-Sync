class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        
        total=sum(nums)
        
        left=nums[:n//2]
        right=nums[n//2:]

        left_sums=[]
        right_sums=[]

        def subsets(idx,curr,arr,res):
            if idx==len(arr):
                res.append(curr)
                return
            subsets(idx+1,curr,arr,res)
            subsets(idx+1,curr+arr[idx],arr,res)
        
        subsets(0,0,left,left_sums)
        subsets(0,0,right,right_sums)
       
        mini=float("inf")


        right_sums.sort()
        
        for x in left_sums:
                needed=goal-x
                idx=bisect.bisect_left(right_sums,needed)

                if idx<len(right_sums):
                    diff1=right_sums[idx]+x
                    mini=min(mini,abs(goal-diff1))
                
                if idx>0:
                    diff2=right_sums[idx-1]+x
                    mini=min(mini,abs(goal-diff2))
        return mini
        
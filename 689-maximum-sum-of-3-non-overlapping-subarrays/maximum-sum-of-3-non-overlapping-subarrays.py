class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:

        n=len(nums)
        w=[0]*(n-k+1)
        curr=sum(nums[:k])
        w[0]=curr
        for i in range(1,n-k+1):
            curr+=nums[i+k-1]-nums[i-1]
            w[i]=curr
        
        left=[0]*len(w)
        best_left=0

        for i in range(len(w)):
            if w[i]>w[best_left]:
                best_left=i 
            left[i]=best_left
        
        right=[0]*len(w)
        best_right=len(w)-1

        for i in range(len(w)-1,-1,-1):

            if w[i]>=w[best_right]:
                best_right=i
            right[i]=best_right
        
        ans=[-1,-1,-1]
        maxi=0

        for i in range(k,len(w)-k):
            l=left[i-k]
            r=right[i+k]

            total=w[l]+w[r]+w[i]
            if total>maxi:
                maxi=total
                ans=[l,i,r]
        return ans
        




        
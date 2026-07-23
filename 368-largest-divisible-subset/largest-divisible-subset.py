class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        n=len(nums)
        nums.sort()

        dp=[0]*n
        prev=[-1]*n
    
        last=0
        maxi=0
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        prev[i]=j
                    if maxi<dp[i]:
                        maxi=dp[i]
                        last=i
                        
        res=[]
        print(dp,maxi)
        print(prev,last)
       
        while last!=-1:
            res.append(nums[last])
            last=prev[last]
        return res[::-1]


        

        
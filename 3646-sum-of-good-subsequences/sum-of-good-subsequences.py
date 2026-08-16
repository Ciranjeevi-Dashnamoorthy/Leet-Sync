class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:

        """
        Observation:

        For any number n in nums, find the n-1 or n+1 in the array
        and add its contribution --> CORE LOGIC

        How do we find its contribution

        any number which is added to the subsequence, its 

        """
        from collections import defaultdict
        
        n=len(nums)
        d=defaultdict(int)
        mod=10**9+ 7
        count=defaultdict(int)
        ans=0

        for i in range(n):
            
            prev=d[nums[i]-1]
            after=d[nums[i]+1]
            c_prev=count[nums[i]-1]
            c_after=count[nums[i]+1]

            new_count=count[nums[i]-1]+1+count[nums[i]+1]
            new_sum=nums[i]

            new_sum=(new_sum+prev + c_prev*(nums[i]))%mod
            new_sum=(new_sum+ after + c_after*(nums[i]))%mod

            count[nums[i]]=count[nums[i]]+new_count
            d[nums[i]]=(d[nums[i]]+new_sum)%mod

            ans=(ans+new_sum)%mod

        return ans





        
class Solution:
    def numOfSubarrays(self, arr):

        n=len(arr)
        odd=0
        even=1
        ans=0
        mod=10**9 + 7
        curr=0

        for i in range(n):
            curr+=arr[i]
            if curr%2==1:
                ans=(ans+even)%mod
                odd+=1
            else:
                ans=(ans+odd)%mod
                even+=1
        return ans

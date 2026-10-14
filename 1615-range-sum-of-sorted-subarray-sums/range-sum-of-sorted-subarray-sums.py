class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:

        n=len(nums)
        arr=[]
        ans=0

        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                arr.append(s)
        arr.sort()
        mod=10**9 + 7
        for i in range(left,right+1):
            ans=(arr[i-1]+ans)%mod
        return ans
            


        
class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:

        m,n=len(arr1),len(arr2)

        ans1=0
        ans=0
        for i in range(m):
            ans1^=arr1[i]
        for i in range(n):
            ans^=(arr2[i]&ans1)
        return ans

        
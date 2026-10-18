class Solution:
    def numOfWays(self, nums: list[int]) -> int:

        mod=10**9 + 7

        def ways(arr):

            if len(arr)<=2:
                return 1
            root=arr[0]
            left=[]
            right=[]

            for num in arr:
                if num<root:
                    left.append(num)
                elif num>root:
                    right.append(num)
            
            curr=math.comb(len(right)+len(left),len(left))

            return (curr*ways(left)*ways(right))%mod
        

        return (ways(nums)-1)%mod
        
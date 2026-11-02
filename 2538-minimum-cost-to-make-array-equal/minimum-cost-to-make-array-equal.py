class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:

        import bisect
class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:

        """
        1- 2
        3 - 4
        to reach 5 2+ 4 
        """
        n=len(nums)
        arr=[]
        check=[]
        for i in range(n):
            arr.append((nums[i],cost[i]))
            check.append(nums[i])
        arr.sort()
        check.sort()
        pref=[0]*(n)
        pref[0]=arr[0][1]
        for i in range(1,n):
            pref[i]=pref[i-1]+arr[i][1]
        
        actual=[0]*(n)
        reverse=[0]*(n)
        s = [0] * (n)
        s[-1] = arr[-1][1]
        for i in range(n-2, -1, -1):
            s[i] = s[i+1] + arr[i][1]
        for i in range(n-2,-1,-1):
            prev=arr[i+1][0]
            curr=arr[i][0]
            diff=prev-curr
            reverse[i]=(diff*s[i+1])+ reverse[i+1]
            
        for i in range(1,n):
            prev=arr[i-1][0]
            curr=arr[i][0]
            diff=curr-prev
            actual[i]=(diff*pref[i-1])+actual[i-1]
        # print(arr)
        # print(pref)
        print(actual)
        print(reverse)
        print(check)
        l=min(nums)
        r=max(nums)
        mini=float("inf")
        for i in range(n):
            curr=actual[i]+reverse[i]
            mini=min(mini,curr)
        return mini

            

        
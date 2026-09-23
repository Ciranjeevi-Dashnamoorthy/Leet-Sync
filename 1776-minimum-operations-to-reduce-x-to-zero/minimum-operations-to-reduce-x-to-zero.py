from collections import defaultdict
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        n=len(nums)
        first=defaultdict(int)
        first[0]=-1
        i=0
        curr=0
        mini1=float("inf")
        mini2=float("inf")
        if sum(nums)<x:
            return -1
        while curr<x:
            curr+=nums[i]
            first[curr]=i
            if curr==x:
                mini1=i+1
            i+=1
        i=n-1
        last=defaultdict(int)
        last[0]=n
        curr=0
        
        while curr<x:
            curr+=nums[i]
            if x-curr in first:
                mini1=min(mini1,first[x-curr]+1+n-i)
            if curr==x:
                mini2=n-i
            last[curr]=i
            i-=1
        
        curr=0
        i=0
        print(mini1,mini2)
        
        while curr<x:
            curr+=nums[i]
            if x-curr in last:
                print(curr,i)
                mini2=min(mini2,n-i+1+last[x-curr])
            i+=1
        print(mini1,mini2)
        ans=min(mini1,mini2)   
        if ans!=float("inf"):
            return ans
        else:
            return -1     
        
                



        
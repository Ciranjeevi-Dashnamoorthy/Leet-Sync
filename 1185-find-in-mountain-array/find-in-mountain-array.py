# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        
        # print(mountainArr.length())
        arr=mountainArr
        n=arr.length()
        l=0
        r=n-1
        peak=0
        val=0
        d=defaultdict(int)
        while l<=r:
            i=(l+r)//2
            print(i)
            prev=arr.get(i-1)
            mid=arr.get(i)
            forw=arr.get(i+1)
            if prev<mid>forw:
                peak=i
                val=mid
                break
            elif prev<mid<forw:
                l=i
            else:
                r=i
        
        if target>val:
            return -1
        if target==val:
            return i
        ans=float("inf")

        l=0
        r=peak-1
        print(l,r)
        while l<=r:
            i=(l+r)//2
            val=arr.get(i)
            if val==target:
                ans=min(ans,i)
                r=i-1
            elif val<target:
                
                l=i+1
            else:
                r=i-1
        l=peak+1
        r=n-1
       
        while l<=r:
            i=(l+r)//2
            val=arr.get(i)
            if val==target:
                ans=min(ans,i)
                r=i-1
            elif val<target:
                r=i-1
            else:
                l=i+1
        return ans if ans!=float("inf") else -1
            


        



        
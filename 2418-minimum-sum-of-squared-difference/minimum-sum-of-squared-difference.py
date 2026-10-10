import heapq
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:

        """
        obs:

        we can perform atmost k1 and k2 times, this means we have to 
        reduce the diff to 0

        after reducing to zero we drop, the mini values we could get
        so bs on mini value , the monotonicity is valid 

        but how do we distirbute the k among all the diff
        there is a problem 

        so we find the minimum threshold diff each can hold by binary serach
        and reduce to it to the ans we find

        the remaining is taken from the largest avail diff 

        """

        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(abs(nums1[i]-nums2[i]))
        
        l=0
        r=max(diff)
        if sum(diff)<=k1+k2:
            return 0
        ans=0
        ops=k1+k2

        while l<=r:
            mid=(l+r)//2
            s=0
            for i in range(n):
                if diff[i]>mid:
                    s+=diff[i]-mid
            
            if s<=ops:
                ans=mid
                r=mid-1
            else:
                l=mid+1
            
        
        rem=0
        s=0
       
        

        for i in range(n):
            s+=max(0,diff[i]-ans)

        rem=ops-s
        
        final=0
        

        for i in range(n):
          
            if diff[i]>=ans:
                if rem>0:
                    final+=(ans-1)**2
                    rem-=1
                else:
                    final+=ans**2
            else:
                final+=diff[i]**2

        return final



        

        
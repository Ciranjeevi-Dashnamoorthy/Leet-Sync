import bisect
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        """
        Observation:

        DP fails why??
        negative numbers 
        total sum being very large

        optimzed app--> generate all subsets with meet in the middle optimization

        split the array onto two parts
        generate the possible subset sum of k elemets 
        k--> 1 to n//2

        iterate by taking the left part elemets 
        and search for the valid sum using bianry search
        """
        n=len(nums)//2
        target=sum(nums)//2
        total=sum(nums)

        left=nums[:n]
        right=nums[n:]

        left_sums=[[] for _ in range(n+1)]
        right_sums=[[] for _ in range(n+1)]

        def subsets(idx,count,curr,arr,res):
            if idx==len(arr):
                res[count].append(curr)
                return
            subsets(idx+1,count,curr,arr,res)
            subsets(idx+1,count+1,curr+arr[idx],arr,res)
        
        subsets(0,0,0,left,left_sums)
        subsets(0,0,0,right,right_sums)
       
        mini=float("inf")

        for i in range(n+1):
            right_sums[i].sort()
        
        for k in range(n+1):
            right_k=n-k
            right_arr=right_sums[n-k]

            for x in left_sums[k]:
                needed=target-x
                idx=bisect.bisect_left(right_arr,needed)

                if idx<len(right_arr):
                    diff1=right_arr[idx]
                    mini=min(mini,abs(total-2*(x+diff1)))
                
                if idx>0:
                    diff2=right_arr[idx-1]
                    mini=min(mini,abs(total-2*(x+diff2)))
        return mini

        
        

        


        
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        n=len(nums)
        from collections import Counter

        if k==1:
            d=Counter(nums)
            maxi=-1
            for num in d:
                if d[num]==1:
                    maxi=max(maxi,num)
            return maxi
        if k==n:
            return max(nums)
        
        # s=set(nums[1:n-1])
        # if nums[0]!=nums[-1]:
        #     maxi=max(nums[0],nums[-1])
        #     if maxi not in s:
        #         return maxi
        #     else:
        #         return -1
        # else:
        #     return -1
        maxi=-1
        from collections import defaultdict
        d=defaultdict(int)
        for i in range(n-k+1):
            for j in range(i,i+k):
                d[nums[j]]+=1

        for num in d:
                if d[num]==1:
                 maxi=max(maxi,num)
        return maxi


        
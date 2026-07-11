class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        """
        Observation:

        split the array into two to get same average
        you cant do simply like subset sum as it is not fixed like sum//2
        it changes depending upon the included elements in the subset

        pts:

        sum(a)+ sum(b)=total

        we need,
        sum(a)/n1 == sum(b)/n2

        based on these two equations, we can deicde

        sum(a)=(total*k)/n

        where can be anything from 1 to n

        PRUNING DONE 

        Now its standard subset sum DP

        maintain subset sum of all possible lengths

        to find the possible lengths we use mod operator

        why <=n//2 because of symmetry

        maintain dp for every possible length and their respective sums and return if on e
        occurs

        """
        
        poss=[]
        total=sum(nums)
        n=len(nums)
        for k in range(1,n//2+1):
            if (total*k)%n==0:
                poss.append(k)
        
        if not poss:
            return False
        
        dp=[set() for _ in range(n//2+1)]
        dp[0].add(0)

        
        
        for num in nums:
            for i in range(n//2,0,-1):
                for prev in dp[i-1]:
                    dp[i].add(prev+num)
        
        
        for p in poss:
            target=(total*p)//n
            if target in dp[p]:
               
                return True

        return False
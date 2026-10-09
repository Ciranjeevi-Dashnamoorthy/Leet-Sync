class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        observation:

        first thing , if total setas are odd return 0

        we know, its eaxctly 2 seats in each section

        curr section ... P P P P P ... Next section starts here

        how can we place dividor , its basically plants + 1 
        we can simply keep track fo the planst btw two sections or 
        the prev index pos

        """
        n=len(s)
        
        mod=10**9+7

        ans=1
        seats=0

        for i in range(n):
            if s[i]=="S":
                seats+=1

                if seats>=3 and seats%2==1:
                    print(seats,prev,i)
                    ans=(ans*(i-prev))%mod
                prev=i
        print(seats)
        if seats<2 or seats%2==1:
            return 0
        return ans 

        
        


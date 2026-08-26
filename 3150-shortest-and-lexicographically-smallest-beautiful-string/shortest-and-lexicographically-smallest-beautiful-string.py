class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        """

        APPROACH 2 
        COUNT ONES AND POS
        
        """

        n=len(s)
        one=[]
        for i in range(n):
            if s[i]=="1":
                one.append(i)
    
        l=0
        m=len(one)
        ans="1"*n
        mini=float("inf")

        for i in range(k-1,m):
            prev=one[i-k+1]
            curr=one[i]
            l=curr-prev+1
            if l<mini:
             ans=s[prev:curr+1]
             mini=l
            elif l<=mini:
                ans=min(ans,s[prev:curr+1])
  
        return ans if mini!=float("inf") else ""
            



        


            
                

        
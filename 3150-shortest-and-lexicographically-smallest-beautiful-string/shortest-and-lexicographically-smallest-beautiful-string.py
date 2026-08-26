class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        n=len(s)
        l=0
        one=0
        mini=float("inf")
        ans="1"*n
        for r in range(n):
            if s[r]=="1":
                one+=1
            
            while one>k or (l<n and s[l]=="0"):
                if s[l]=="1":
                    one-=1
                l+=1

                
                if one==k and r-l+1<=mini:
                 
                 if mini==r-l+1:
                    ans=min(ans,s[l:r+1])
                 else:
                  ans=s[l:r+1]
                 mini=r-l+1
            if one==k and r-l+1<mini:
             mini=r-l+1
             ans=s[l:r+1]
            
        return ans if mini!=float("inf") else ""


            
                

        
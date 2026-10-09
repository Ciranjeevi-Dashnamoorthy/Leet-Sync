class Solution:
    def minInsertions(self, s: str) -> int:

        n=len(s)
        ans=0
        ope=0
        i=0
        
        while i<n:

            if s[i]=="(":
                ope+=1
            else:
                if i<n-1 and s[i+1]==")":
                    i+=1
                else:
                    ans+=1
                if ope>0:
                    ope-=1
                else:
                    ans+=1
            i+=1
        return ans+2*ope


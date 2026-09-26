class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        from collections import defaultdict

        d={}

        for k,v in knowledge:
            d[k]=v
        
        i=0
        ans=""
        n=len(s)
        while i<n:

            if s[i]=="(":
                curr=""
                i+=1
                while s[i]!=")":
                    curr+=s[i]
                    i+=1
                if curr in d:
                    ans+=d[curr]
                else:
                    ans+="?"
            else:
                ans+=s[i]
            i+=1
        return ans

                

        
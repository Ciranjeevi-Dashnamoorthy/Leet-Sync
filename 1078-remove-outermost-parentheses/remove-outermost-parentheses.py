class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        n=len(s)
        curr=0
        res=""
        for i in range(n):
            if s[i]=="(":
                if curr>0:
                    res+=s[i]
                curr+=1
                
            else:
                curr-=1
                if curr>0:
                    res+=s[i]
        return res
                  
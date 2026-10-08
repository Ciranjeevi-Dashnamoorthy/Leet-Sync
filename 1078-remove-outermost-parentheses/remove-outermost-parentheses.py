class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        n=len(s)
        stack=[]
        res=""
        for i in range(n):
            if s[i]=="(":
                if stack:
                    res+=s[i]
                stack.append("(")
                
            else:
                stack.pop()
                if stack:
                    res+=s[i]
        return res
                  
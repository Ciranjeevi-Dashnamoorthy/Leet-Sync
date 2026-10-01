class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]

        d={"(":")","{":"}","[":"]"}
        for i in range(n):
            if s[i] in d:
                stack.append(s[i])

            else:
                if len(stack)>0 and d[stack[-1]]==s[i]:
                    stack.pop()
                else:
                    return False
                
        return True if len(stack)==0 else False            
        
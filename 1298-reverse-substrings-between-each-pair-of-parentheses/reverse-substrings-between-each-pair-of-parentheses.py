class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack=[]
        n=len(s)

        for i in range(n):
            if s[i]=="(":
                stack.append("(")
            else:
                if s[i]==")":
                    curr=""
                    while stack[-1]!="(":
                        curr+=stack.pop()
                    stack.pop()
                    for ch in curr:
                        stack.append(ch)
                else:
                    stack.append(s[i])
        return "".join(stack)

                
        
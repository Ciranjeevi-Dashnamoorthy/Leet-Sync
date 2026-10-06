class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack=[]
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(")")
        return len(stack)
        
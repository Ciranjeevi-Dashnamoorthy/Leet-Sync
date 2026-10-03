class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        n=len(s)
        m=0

        for i in range(n):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    m=max(m,i-stack[-1])
        return m
        
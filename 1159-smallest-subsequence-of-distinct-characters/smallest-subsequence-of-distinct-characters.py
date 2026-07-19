class Solution:
    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter

        d=Counter(s)
        stack=[]
        vis=set()
        n=len(s)

        for i in range(n):
            d[s[i]]-=1

            if s[i] in vis:
                continue
            
            while stack and s[i]<stack[-1] and d[stack[-1]]>0:
                val=stack.pop()
                vis.remove(val)
            
            vis.add(s[i])
            stack.append(s[i])
            
        return "".join(stack)
        


        
class Solution:
    def minOperations(self, s: str) -> int:

        order=sorted(s)
        n=len(s)
        first=order[0]
        last=order[-1]
        
        if "".join(order)==s:
            return 0
        if n==2 and last==s[0] and first==s[-1]:
            return -1

        if first==s[0] or last==s[-1]:
            return 1
        elif first not in s[0:n-1] and  last not in s[1:n]:
            return 3
        else:
            return 2
    
            
        
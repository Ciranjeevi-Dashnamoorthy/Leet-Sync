class Solution:
    def reverseDegree(self, s: str) -> int:

        n=len(s)
        ans=0
        for i in range(n):
            ans+=((i+1)*(26-ord(s[i])+ord("a")))
           
        return ans

        
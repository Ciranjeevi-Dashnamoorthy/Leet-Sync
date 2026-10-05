class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        
        n=len(s)
        score=0
        curr=0
        
        if s[0]=="(":
            curr+=1
        else:
            curr-=1
        for i in range(1,n):
            if s[i]=="(":
                curr+=1
            else:
                curr-=1
            
            if s[i-1]=="(" and s[i]==")":
                score+=2**curr
        return score

                
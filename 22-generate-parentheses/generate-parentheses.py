class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]

        def backtrack(openN,closedN,stack):
            if len(stack)==2*n:
                res.append("".join(stack))
                return
            if openN<n:
                
                stack.append("(")
                backtrack(openN+1,closedN,stack)
                stack.pop()
            if closedN<openN:
                 stack.append(")")
                 backtrack(openN,closedN+1,stack)
                 stack.pop()
            
           
        backtrack(0,0,[])
        return res
            
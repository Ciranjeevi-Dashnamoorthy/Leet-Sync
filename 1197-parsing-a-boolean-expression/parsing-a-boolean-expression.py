class Solution:
    def parseBoolExpr(self,s: str) -> bool:

        """
        stack
        """

        stack=[]
        n=len(s)
        i=0
        g=True

        while i< n:
            if (s[i]=="!" or s[i]=="|" or s[i]=="&") or ( i<n-1 and ((s[i]=="t" and s[i+1]==",") or (s[i]=="f" and s[i+1]==","))):
                stack.append(s[i])
                i+=2
            elif s[i]=="f" or s[i]=="t" :
                stack.append(s[i])
                i+=1
            elif s[i]==",":
                i+=1
            else:
                curr=[]
                
                while stack :
                    if stack[-1]=="&" or stack[-1]=="!" or stack[-1]=="|":
                        exp=stack[-1]
                        stack.pop()
                        break
                    b=stack.pop()
                    if b=="t":
                        curr.append(1)
                    else:
                        curr.append(0)
                
                if exp=="&":
                    ans=1
                    for k in range(len(curr)):
                        ans&=curr[k]
                elif exp=="|":
                    ans=0
                    for k in range(len(curr)):
                        ans|=curr[k]
                else:
                    
                    for k in range(len(curr)):
                        if curr[k]==1:
                            ans=0
                        else:
                            ans=1
                stack.append( "t" if ans else "f")
                i+=1
                
        return True if stack[-1]=="t" else False

                



        
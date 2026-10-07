class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        n=len(s)
        res=[]
        maxi=0
        @cache
        def dp(idx,path,diff):
            nonlocal maxi
            if idx>=n:
                if diff==0:
                    maxi=max(maxi,len(path))
                    res.append(path)
                return
            if diff<0:
                return
            if s[idx] not in "()":
                dp(idx+1,path+s[idx],diff)
                
            else:
                dp(idx+1,path,diff)
                
                if s[idx]=="(":
                    diff+=1
                else:
                    diff-=1
                dp(idx+1,path+s[idx],diff)
                
        dp(0,"",0)
        
        ans=[]
        for i in range(len(res)):
            if len(res[i])==maxi :
               
                ans.append(res[i])
                    
        return ans

        
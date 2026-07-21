class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)

        ans=[]
        curr=0
        one=0
        for i in range(n):
            if s[i]=="0":
                curr+=1
            else:
                if curr>0:
                    ans.append(curr)
                curr=0
                one+=1
        if curr>0:
            ans.append(curr)
        if len(ans)<2:
            return one
        val=0
        print(ans)
        for i in range(len(ans)-1):
            val=max(ans[i]+ans[i+1],val)
            
            

            
        return val+one


        
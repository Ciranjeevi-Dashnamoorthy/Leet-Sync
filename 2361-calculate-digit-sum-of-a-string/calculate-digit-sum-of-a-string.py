class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s)>k:
            n=len(s)
            curr=0
            ans=""
            tot=0

            for i in range(n):
                curr+=1
                tot+=int(s[i])
                if curr==k:
                    curr=0
                    ans+=str(tot)
                    tot=0
            if curr>0:
                ans+=str(tot)
            s=ans
        return s

      
        

        
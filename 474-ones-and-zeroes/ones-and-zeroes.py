class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        le=len(strs)
        
        @cache
        def solve(i,j,k,ct):
            if i==le:
                return ct
           
            noskip=0
            skip=solve(i+1,j,k,ct)
            
            one=0
            zero=0
            p=len(strs)
            for ch in strs[i]:
                if ch=="1":
                    one+=1
                else:
                    zero+=1
           
            if zero+j<=m and one+k<=n:
                noskip=solve(i+1,zero+j,one+k,ct+1)
            ways=max(skip,noskip)
            
            return ways

        

        ans=solve(0,0,0,0)
        return ans

        
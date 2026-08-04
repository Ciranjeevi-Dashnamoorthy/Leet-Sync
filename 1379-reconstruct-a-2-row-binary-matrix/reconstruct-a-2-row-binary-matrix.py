class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n=len(colsum)
        ans=[[0]*n for _ in range(2)]
        up,low=0,0


        for i in range(n):

            v1=colsum[i]//2 + colsum[i]%2
            v2=colsum[i]//2

            ans[0][i]=v1
            ans[1][i]=v2
            up+=ans[0][i]
            low+=ans[1][i]
        
        updiff=upper-up
        lowdiff=lower-low
        if abs(updiff)!=abs(lowdiff) or sum(colsum)!=(upper+lower):
            return []
      
        

        for i in range(n):
            if updiff>0:
                diff=min(abs(ans[0][i]-ans[1][i]),updiff)
                diff=max(diff,0)
                updiff-=diff
                lowdiff+=diff
                
                ans[0][i]+=diff
                ans[1][i]-=diff
                
            if lowdiff>0:
                diff=min(abs(ans[1][i]-ans[0][i]),lowdiff)
                diff=max(diff,0)
                lowdiff-=diff
                updiff+=diff
                ans[1][i]+=diff
                ans[0][i]-=diff
            print(updiff,lowdiff)
            if ans[0][i]<0 or ans[1][i]<0:
                    return []
          
        return ans if lowdiff==0 and updiff==0 else []
            



        
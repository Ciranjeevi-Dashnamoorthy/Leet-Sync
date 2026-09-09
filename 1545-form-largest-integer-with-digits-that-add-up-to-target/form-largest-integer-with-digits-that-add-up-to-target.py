class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        dp=[float("-inf")]*(target+1)
        dp[0]=0
        

        for i in range(1,target+1):
            for j in range(1,9+1):
                c=cost[j-1]
                
                if i-c>=0 and dp[i-c]!=float("-inf"):
                    
                    curr=dp[i-c]+1
                    if curr>dp[i]:
                        dp[i]=curr
        
        if dp[-1]==float("-inf"):
            return "0"
      
        curr=target
        ans=""
        for d in range(9,0,-1):
            c=cost[d-1]
            while curr>=c and dp[curr]==dp[curr-c]+1:
                ans+=str(d)
                curr-=c
        return ans 
  


        
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        from collections import defaultdict        
        l=0
        ans=0
        n=len(s)
        curr=defaultdict(int)
        for r in range(n):
            curr[s[r]]+=1
            
            while curr[s[r]]>2:
                curr[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans

                


class Solution:
    def distinctEchoSubstrings(self, s: str) -> int:
        n=len(s)
        vis=set()
        ans=0
        counted=set()
        for l in range(1,n+1):
            for i in range(l,n-l+1):
                
                left=s[i-l:i]
                right=s[i:i+l]
                

                if left==right and left not in vis:
                    ans+=1
                    vis.add(left)
        return ans

        
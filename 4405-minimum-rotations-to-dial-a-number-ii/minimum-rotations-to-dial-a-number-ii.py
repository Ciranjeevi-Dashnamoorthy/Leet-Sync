class Solution:
    def minRotations(self, n: int, s: str) -> int:

        ans=0
        prev=0
        diff=0

        def calc(a,b):
            dist=abs(a-b)
            rev=10-dist
            rot=min(dist,rev)
            return rot
        for i in range(n):
            curr=int(s[i])
            rot=calc(prev,curr)
            if i<n-1:
                ac=calc(prev,int(s[n-1]))
               
                if rot>ac:
                    diff=max(diff,rot-ac)
                    
            prev=curr
            ans+=rot
        return min(ans,ans-diff)


        
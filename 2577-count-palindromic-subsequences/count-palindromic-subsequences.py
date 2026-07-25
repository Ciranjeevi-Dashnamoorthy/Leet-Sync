class Solution:
    def countPalindromes(self, s: str) -> int:

        """
        A B C B A
        valid palindrome of length five

        make c as Center
        we check for ab and ba occurences on eac side and multiply it 

        ans += left * right 

        Precompuatation of all poss occurences from 00-99

        first we need right precomp and we can gen left on go

        """
        n=len(s)
        mod=10**9 + 7

        r1=[0]*10
        r2=[[0]*10 for _ in range(10)]
        l1=[0]*10
        l2=[[0]*10 for _ in range(10)]

        for i in range(n-1,-1,-1):
            curr=int(s[i])
            for d in range(10):
                r2[curr][d]+=r1[d]
            r1[curr]+=1
        
        ans=0
        for i in range(n):
            curr=int(s[i])
            r1[curr]-=1
            for d in range(10):
                r2[curr][d]-=r1[d]
            
            for x in range(10):
                for y in range(10):

                    if l2[x][y]>0 and r2[y][x]>0:
                        ans=(ans+l2[x][y]*r2[y][x])%mod
            
            for d in range(10):
                l2[d][curr]+=l1[d]
            l1[curr]+=1
        return ans
            

        
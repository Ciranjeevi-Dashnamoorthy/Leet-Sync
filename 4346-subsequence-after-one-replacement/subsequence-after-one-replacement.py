class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:

        m,n=len(s),len(t)

        pref=[float("inf")]*m
        suff=[float("-inf")]*m
        j=0
        for i in range(m):
            while j<n and s[i]!=t[j]:
                j+=1
            if j==n:
                break
            pref[i]=j
            j+=1
        
        if pref[-1]!=float("inf"):
            return True
        print(pref)
        print(suff)
        j=n-1
        for i in range(m-1,-1,-1):
            while j>=0 and s[i]!=t[j]:
                j-=1
            if j<0:
                break
            suff[i]=j
            j-=1
        

        for i in range(m):
            if i==0:
                u=-1
            else:
                u=pref[i-1]
            if i==m-1:
                v=n
            else:
                v=suff[i+1]
            if u!=float("inf") and v!=float("-inf") and u<v-1:
                return True
        return False
        
        
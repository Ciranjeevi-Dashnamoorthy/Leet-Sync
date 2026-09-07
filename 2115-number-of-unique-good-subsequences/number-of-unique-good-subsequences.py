class Solution:
    def numberOfUniqueGoodSubsequences(self, s: str) -> int:

        n=len(s)
        fl=False
        one=0
        zero=0
        mod=10**9+7

        for i in range(n):
            if s[i]=="1":
                one=(one+zero+1)%mod
            else:
                zero=(one+zero)%mod
                fl=True
        return (one+zero+fl)%mod
                

        
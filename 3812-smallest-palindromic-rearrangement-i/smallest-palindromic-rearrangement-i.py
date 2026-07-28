class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        d=Counter(s)
        res=[]
        middle=""
        for i in d:
            
            if d[i]%2==1:
                middle=i
            for j in range(d[i]//2):
                res.append(i)
        
        res.sort()
      
        ans="".join(res)
        return ans+middle+ans[::-1]
        
        
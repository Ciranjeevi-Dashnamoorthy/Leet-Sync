class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        first=[-1]*26
        last=[-1]*26
        n=len(s)
        total=0

        for i in range(n):
            char=ord(s[i])-97
            if last[char]==-1:
                first[char]=i
            last[char]=i
        
        for i in range(26):
            left=first[i]
            right=last[i]
            
            if left!=-1 and right-left>1:

                seen=set( )
                ct=0
                for k in range(left+1,right):
                    inner=ord(s[k])-97

                    if inner not in seen:
                        ct+=1
                        seen.add(inner)
                total+=ct
        return total
                    

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        for each indice count the no of substring it presents

        -1 idx1 idx2 n

        for idx1
        the ct of subarray is 
        left sum= idx1-(-1)
        right sum-idx2-idx1

        total ct= left*right 
        """

        from collections import defaultdict

        d=defaultdict(list)
        for i in range(65,91):
            d[chr(i)].append(-1)
        ans=0
        n=len(s)

        for i in range(n):
            d[s[i]].append(i)
        
        for char in d:
            d[char].append(n)

            arr=d[char]
     
            for i in range(1,len(arr)-1):
                left=arr[i-1]
                curr=arr[i]
                right=arr[i+1]
                ans+=(curr-left)*(right-curr)
        return ans


        
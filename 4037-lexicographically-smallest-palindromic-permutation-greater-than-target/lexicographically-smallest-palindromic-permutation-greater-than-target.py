class Solution:
    def lexPalindromicPermutation(self, s: str, t: str) -> str:

        """
        Observation:

        similar to yesterdays one , just find the possible arrnagemnt for first n//2 length
        and create a palindrome


        for the current index , check we can place the element which equals target
        after placing, check can we generate a larger permutation

        if we cant generate or we dont have any charcters to build, then
        it completely breaks
        we just find the next greater element which can be placed after 
        curr in target
        after placing that one element 
        build the smallest segment after it 

        if we cant find somehting greater than the current element 
        return ""

        """
        from collections import Counter

        n=len(s)
        d=Counter(s)
        res=[]
        ct=0
        middle=""
        for ch in d:
            if d[ch]%2==1:
                ct+=1
                middle=ch
            if ct==2:
                return ""

        for i in range(n//2+1):
            curr=t[i]

            if d[curr]>=2:

                d[curr]-=2
                larg=[]
                for idx in range(25,-1,-1):
                    ch=chr(idx+ord("a"))
                    if d[ch]>0:
                        larg.append((d[ch]//2)*ch)  
              
                palin="".join(larg)+middle+"".join(larg[::-1])+curr+"".join(res[::-1])
                if palin>t[i+1:]:
                    res.append(curr)
                    continue
                d[curr]+=2

          

            for idx in range(ord(curr)-ord("a")+1,26):
                ch=chr(idx+ord("a"))
           
                if d[ch]>1:
                    d[ch]-=2
                    res.append(ch)
                    small=[]

                    for j in range(26):
                        ch=chr(j+ord("a"))
                        if d[ch]>0:
                            small.append((d[ch]//2)*ch)
                    palin="".join(res)+"".join(small)+middle + "".join(small[::-1])+"".join(res[::-1])
                    return palin
            part= 1 if middle!="" else 0
            if len(res)*2+part==n:
                palin="".join(res)+middle+"".join(res[::-1]) 
                if palin>t:
                    return palin
            return ""           

        
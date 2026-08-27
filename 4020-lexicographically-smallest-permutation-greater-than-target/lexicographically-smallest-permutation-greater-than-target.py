class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:

        """
        Observation:

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

        for i in range(n):
            curr=t[i]

            if d[curr]>0:

                d[curr]-=1
                larg=[]
                for idx in range(25,-1,-1):
                    ch=chr(idx+ord("a"))
                    if d[ch]>0:
                        larg.append(d[ch]*ch)  
                if "".join(larg)>t[i+1:]:
                    res.append(curr)
                    continue
                d[curr]+=1

            for idx in range(ord(curr)-ord("a")+1,26):
                ch=chr(idx+ord("a"))
                if d[ch]>0:
                    d[ch]-=1
                    res.append(ch)
                    small=[]

                    for j in range(26):
                        ch=chr(j+ord("a"))
                        if d[ch]>0:
                            small.append(d[ch]*ch)

                    return "".join(res)+"".join(small) 
            return ""           

        
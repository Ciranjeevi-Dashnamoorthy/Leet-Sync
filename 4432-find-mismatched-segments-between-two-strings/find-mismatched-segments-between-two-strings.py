class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:

        n=len(s1)

        res=[]
        curr1=""
        curr2=""
        for i in range(n):
            if s1[i]!=s2[i]:
                curr1+=s1[i]
                curr2+=s2[i]
            else:
                if curr1!="":
                    res.append([curr1,curr2])
                curr1=""
                curr2=""
        if curr1!="":
            res.append([curr1,curr2])
            curr1=""
            curr2=""
        return res


        
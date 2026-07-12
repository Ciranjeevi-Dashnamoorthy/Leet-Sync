class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        s=sorted(arr)
        n=len(arr)
        d={}
        ct=1
        for i in range(n):
            if s[i] not in d:
                d[s[i]]=ct
                ct+=1
        
        res=[]
        for i in range(n):
            res.append(d[arr[i]])
        return res
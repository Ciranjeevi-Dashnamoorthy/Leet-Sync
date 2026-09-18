class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        
        d=defaultdict(list)
        n=len(s)
        intervals=[]
        for i in range(n):
            if s[i] not in d:
                d[s[i]].append(i)
                d[s[i]].append(i)
            else:
                d[s[i]][1]=i
        
        for ch in set(s):
            start=d[ch][0]
            end=d[ch][1]

            j=start
            fl=True
            while j<=end:
                curr=s[j]
                
                if d[curr][0]<start:
                    fl=False
                    break
                end=max(end,d[curr][1])
                j+=1
            if fl:
                intervals.append([start,end])
        
        intervals.sort(key=lambda x:x[1])

        res=[]
        prev=-1
        for l,r in intervals:
            if l>prev:
                res.append(s[l:r+1])
                prev=r
        return res

            

            

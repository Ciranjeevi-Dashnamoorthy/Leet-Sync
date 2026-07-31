class Solution:
    def minimumPushes(self, word: str) -> int:
        
        from collections import Counter

        d=Counter(word)
        res=[]
        for i in d:
            res.append([d[i],i])
        res.sort(reverse=True)
        inc=1
        curr=0
        ans=0
        print(res)
        for i in range(len(res)):
            ans+=inc*res[i][0]
            curr+=1
            if curr==8:
                curr=0
                inc+=1
        return ans
            
        
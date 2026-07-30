class Solution:
    def minimumPushes(self, word: str) -> int:
        
        inc=1
        curr=0
        ans=0
        for i in range(len(word)):
            ans+=inc
            curr+=1
            if curr==8:
                inc+=1
                curr=0
        return ans
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)

        n=len(words)
        dp={}
        maxi=0

        for word in words:
            dp[word]=1

            for i in range(len(word)):
                pred=word[:i]+word[i+1:]
                
                if pred in dp:
                    dp[word]=max(dp[word],dp[pred]+1)
            maxi=max(maxi,dp[word])
        return maxi





        

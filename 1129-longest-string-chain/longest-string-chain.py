class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        """
        Observation:

        the length of the sequence is always increasing in nature

        we iteate from bottom to top

        if current word abcd --> bcd,acd,abd,abc can only be predecessor 
        so we check for the occurence and the max children they could have 
        iteratively

        implement it using Hash table with key as word and count as value
        """
        
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





        

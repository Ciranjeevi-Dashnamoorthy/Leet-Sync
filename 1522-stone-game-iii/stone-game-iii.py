class Solution:
    def stoneGameIII(self, arr: List[int]) -> str:

        d={}
        def dp(i):
            if i>=n:
                return 0
            if i in d:
                return d[i]

            best=float("-inf")
            score=0

            for x in range(1,4):
                if i+x>n:
                    break
                score+=arr[i+x-1]
                best=max(best,score-dp(i+x))
            d[i]=best
            return best
        
        n=len(arr)
        bal=dp(0)

        if bal<0:
            return "Bob"
        elif bal>0:
            return "Alice"
        return "Tie"

        
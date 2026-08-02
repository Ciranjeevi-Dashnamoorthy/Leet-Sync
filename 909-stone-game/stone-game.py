class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        i,j=0,n-1
        alice,bob=0,0
        fl=True

        while i<j:
            if fl:
                if piles[i]>piles[j]:
                    alice+=piles[i]
                    i+=1
                else:
                    alice+=piles[j]
                    j-=1
            else:
                if piles[i]>piles[j]:
                    bob+=piles[i]
                    i+=1
                else:
                    bob+=piles[j]
                    j-=1
        return True if alice>bob else False


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1=rec1[0]
        r1=rec1[2]
        b1=rec1[1]
        h1=rec1[3]

        l2=rec2[0]
        r2=rec2[2]
        b2=rec2[1]
        h2=rec2[3]

      
        if  ( b1>=h2 or h1<=b2):
            return False
        
        if ( r1<=l2 or l1>=r2):
            return False

        return True
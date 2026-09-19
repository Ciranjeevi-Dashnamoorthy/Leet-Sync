class Solution:
    def minimumBoxes(self, n: int) -> int:

        curr=0
        floor=0
        total=0

        while total+(curr+1+floor)<=n:
            curr+=1
            floor+=curr
            total+=floor
        
        extra=0
        while total<n:
            extra+=1
            floor+=1
            total+=extra
        return floor

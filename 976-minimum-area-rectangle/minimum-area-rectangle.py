class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        n=len(points)
        ans=float("inf")
        s=set()
        for x,y in points:
            s.add((x,y))
        for i in range(n):
            for j in range(i+1,n):

                x1,y1=points[i]
                x2,y2=points[j]

                if x1!=x2 and y1!=y2:

                    ax1,ay1=x1,y2
                    ax2,ay2=x2,y1
                    

                    if (ax1,ay1) in s and (ax2,ay2) in s:
                        area=abs(y2-y1)*abs(x1-x2)
                        ans=min(ans,area)
        return ans if ans!=float("inf") else 0
            
        
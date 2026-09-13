class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        for every two points find the slope and those with macthing slopes 
        are counted
        """
        from collections import defaultdict
        d=defaultdict(int)
        n=len(points)
        m=0
        poss=set()

        for i in range(n):
            d=defaultdict(int)
            for j in range(n):
                if i==j:
                    continue

                x1,y1=points[i]
                x2,y2=points[j]
                
                dx=x2-x1
                dy=y2-y1
                
                
                if dx==0: 
                    d["inf"]+=1
                else:
                    d[dy/dx]+=1
            
            for slope in d:
                ans=d[slope]
                m=max(ans,m)
        return m+1
                        



        

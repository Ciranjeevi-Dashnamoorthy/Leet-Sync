class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        
        import heapq

        def check(r,c):
            if 0<=r<m and 0<=c<n:
                return True
            return False

        heap=[(1,0,0,1)]
        vis=set()
        
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        mini=float("inf")
        while heap:
            cost,r,c,parity=heapq.heappop(heap)
          
            
            
            if (r,c,parity) in vis:
                continue 
           
            vis.add((r,c,parity))
            if r==m-1 and c==n-1:
                return cost
            
            if (r, c,parity^1) not in vis:
                wait_cost = cost + penalty[r][c]
                heapq.heappush(heap, (wait_cost, r, c, parity^1))
            

            if parity%2==1:
                nr,nc=r,c+1
                right=float("inf")
                down=float("inf")
                if check(nr,nc):
                    right=(nr+1)*(nc+1)
                    if (nr,nc,parity^1) not in vis:
                        
                        heapq.heappush(heap,(cost+right,nr,nc,parity^1))
                nr,nc=r+1,c
                if check(nr,nc):
                    down=(nr+1)*(nc+1)
                    if (nr,nc,parity^1) not in vis:
                        
                        heapq.heappush(heap,(cost+down,nr,nc,parity^1))

                nr,nc=r,c-1
                left=float("inf")
                up=float("inf")
                if check(nr,nc):
                    left=(nr+1)*(nc+1)+penalty[r][c]
                    if (nr,nc,parity^1) not in vis:
                        
                        heapq.heappush(heap,(cost+left,nr,nc,parity^1))
                nr,nc=r-1,c
                if check(nr,nc):
                    up=(nr+1)*(nc+1)+penalty[r][c]
                    if (nr,nc,parity^1) not in vis:
                     
                        heapq.heappush(heap,(cost+up,nr,nc,parity^1))
            else:
                nr,nc=r,c-1
                left=float("inf")
                up=float("inf")
                if check(nr,nc):
                    left=(nr+1)*(nc+1)
                    if (nr,nc,parity^1) not in vis:
                       
                        heapq.heappush(heap,(cost+left,nr,nc,parity^1))
                nr,nc=r-1,c
                if check(nr,nc):
                    up=(nr+1)*(nc+1)
                    if (nr,nc,parity^1) not in vis:
                     
                        heapq.heappush(heap,(cost+up,nr,nc,parity^1))
                
                nr,nc=r,c+1
                right=float("inf")
                down=float("inf")
                if check(nr,nc):
                    right=(nr+1)*(nc+1)+penalty[r][c]
                    if (nr,nc,parity^1) not in vis:
                   
                        heapq.heappush(heap,(cost+right,nr,nc,parity^1))
                nr,nc=r+1,c
                if check(nr,nc):
                    down=(nr+1)*(nc+1)+penalty[r][c]
                    if (nr,nc,parity^1) not in vis:
                  
                        heapq.heappush(heap,(cost+down,nr,nc,parity^1))
       
                    
            
            
                        






        
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:

        
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        s,e=0,0
        key="abcdef"
        lock="ABCDEF"
        m,n=len(grid),len(grid[0])
        target=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in key:
                    target|=1<<key.index(grid[i][j])
                if grid[i][j]=="@":
                    s,e=i,j
        queue=deque([(s,e,0,0)])
        vis=set((s,e,0))
       
        while queue:
            r,c,mask,moves=queue.popleft()
            if mask==target:
                return moves

            for i,j in dirs:
                nr,nc=i+r,j+c 
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]!="#":
                    new=mask
                    if grid[nr][nc] not in ".#":
                        ch=grid[nr][nc]

                        if ch in key:
                            idx=key.index(ch.lower())
                            new|=1<<idx
                            
                        elif ch in lock:
                            idx=key.index(ch.lower())
                            req=1<<idx
                            if mask&req!=req:
                                continue
                    if (nr,nc,new) not in vis:
                        queue.append((nr,nc,new,moves+1))
                        vis.add((nr,nc,new))
        return -1
                        





        
        
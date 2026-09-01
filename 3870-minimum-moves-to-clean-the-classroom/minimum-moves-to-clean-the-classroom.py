class Solution:
    def minMoves(self, grid: List[str], energy: int) -> int:

        """
        Observation
        BFS from start and collect all the litters
        how do we track visited , we can revisit the cell based on our priority

        1) we dont care abt the mini steps as bfs ensures it
        2) we need r,c as basic state and curr egy and steps to maintain
        3) using bits for litters , why l<=10

        
        """
        from collections import deque

        m,n=len(grid),len(grid[0])

        lid={}

        vis=[[[0]*10 for _ in range(n)] for _ in range(m)]
        idx=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="L":
                    lid[(i,j)]=idx 
                    idx+=1 
                if grid[i][j]=="S":
                    si,sj=i,j                  

        queue=deque([(si,sj,energy,0,0)])

        vis={(si,sj,0):energy}
    

        # BFS STATE --> (ROW,COL,CURR_ENERGY,STEPS,MASK(LITTER))

        dirs=[(1,0),(0,1),(0,-1),(-1,0)]

        while queue:
            r,c,curr_energy,steps,mask=queue.popleft()
            if mask== 2**idx -1:
                return steps
            
            for x,y in dirs:
                nr,nc=r+x,c+y
                
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]!="X" and curr_energy>=1:

                    new_mask=mask
                    new_energy=curr_energy-1
                    
                    if grid[nr][nc]=="L":
                        shift=lid[(nr,nc)]
                        new_mask=mask | 1<<shift
                                               
                    elif grid[nr][nc]=="R":
                        new_energy=energy
                    
                        
                    if (nr,nc,new_mask) not in vis or new_energy > vis[(nr,nc,new_mask)] :
                            queue.append((nr,nc,new_energy,steps+1,new_mask))
                            vis[(nr,nc,new_mask)]=new_energy 

        return -1
                






        
        
class Solution:
    def containVirus(self, grid: list[list[int]]) -> int:

        m,n=len(grid),len(grid[0])

        dirs=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c,reg,threat):

            vis.add((r,c))
            reg.append((r,c))
            walls=0
            for x,y in dirs:
                nr,nc=x+r,y+c
                if 0<=nr<m and 0<=nc<n:
                    if grid[nr][nc]==1 and (nr,nc) not in vis:
                        walls+=dfs(nr,nc,reg,threat)
                    elif grid[nr][nc]==0:
                        threat.add((nr,nc))
                        walls+=1
            return walls

        total=0
        while True:

            vis=set()
            regions=[]
            threatened=[]
            walls_needed=[]
            for i in range(m):
                for j in range(n):
                    reg=[]
                    threat=set()
                    walls=0

                    if grid[i][j]==1 and (i,j) not in vis:

                        walls+=dfs(i,j,reg,threat)
                        regions.append(reg)
                        threatened.append(threat)
                        walls_needed.append(walls)
            
            if not regions:
                break
            
            maxi=0
            idx=-1
            for i in range(len(threatened)):
                if len(threatened[i])>maxi:
                    maxi=len(threatened[i])
                    idx=i
            print(walls_needed,regions,threatened)
            
            if idx==-1:
                break
            
            for r,c in regions[idx]:
                grid[r][c]=2
            total+=walls_needed[idx]
            
            for i in range(len(threatened)):
                if i!=idx:
                    for r,c in threatened[i]:
                        grid[r][c]=1
        
        return total

            


        
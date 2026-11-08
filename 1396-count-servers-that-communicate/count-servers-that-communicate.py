class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        row=[False for _ in range(m)]
        col=[False for _ in range(n)]
        ct=0
        vis=set()
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]==0:
                    continue
                fl=False
                for k in range(n): 
                    print(i,k)
                    if  j!=k and grid[i][k]==1:
                        fl=True
                
                for l in range(m):
                   
                    if  l!=i and grid[l][j]==1:
                        fl=True                
                if fl:
                    ct+=1
        return ct


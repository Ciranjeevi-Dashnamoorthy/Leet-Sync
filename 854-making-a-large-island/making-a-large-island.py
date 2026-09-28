class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:

        n=len(grid)
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        d={}
        def dfs(r,c,idx):
            d[(r,c)]=idx
            ans=1
            for x,y in dirs:
                nr,nc=x+r,y+c
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in d and grid[nr][nc]==1:
                    ans+=dfs(nr,nc,idx)
            return ans


        curr=0
        idcount={}
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in d:
                    count=dfs(i,j,curr)
                    
                    idcount[curr]=count
                    curr+=1
        if not d:
            return 1
        ans=max(idcount.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    vis=set()
                    contri=1
                    for x,y in dirs:
                        nr,nc=i+x,j+y
                        if 0<=nr<n and 0<=nc<n and grid[nr][nc]==1:
                         currid=d[(nr,nc)]
                         if currid not in vis:
                            contri+=idcount[currid]
                            vis.add(currid)
                    ans=max(ans,contri)
        return ans



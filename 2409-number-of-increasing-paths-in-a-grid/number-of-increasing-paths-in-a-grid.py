class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
    
        m,n=len(grid),len(grid[0])
        mod=10**9 + 7

        @cache
        def dfs(r,c):
            
            if r>=m or c>=n:
                return 0
            dirs=[(1,0),(0,1),(-1,0),(0,-1)]
            ans=1
            for x,y in dirs:
                nr,nc=x+r,c+y
                if 0<=nr<m and 0<=nc<n and grid[r][c]<grid[nr][nc]:
                    ans=(ans+dfs(nr,nc))%mod
            return ans

        ans=0
        for i in range(m):
            for j in range(n):
               
                ans=(ans+dfs(i,j))%mod
        return ans      
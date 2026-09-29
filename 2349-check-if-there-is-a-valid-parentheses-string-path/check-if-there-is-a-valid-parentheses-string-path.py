class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m,n=len(grid),len(grid[0])

        @cache
        def dfs(r,c,ope,close):
            if r>=m or c>=n:
                return False

            
            if grid[r][c]=="(":
                ope+=1
            else:
                close+=1
            if r==m-1 and c==n-1 and ope==close:
                return True
            if ope>=close:
                right=dfs(r,c+1,ope,close)
                down=dfs(r+1,c,ope,close)
                return right or down
            else:
                return False
            


        return dfs(0,0,0,0)
        
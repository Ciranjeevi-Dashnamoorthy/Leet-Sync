class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m,n=len(grid),len(grid[0])

        ans=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                
                new_j=(k+j)%n
                new_i=(i+(k+j)//n)%m
                print(new_i,new_j)
                
                ans[new_i][new_j]=grid[i][j]
        return ans




        


        
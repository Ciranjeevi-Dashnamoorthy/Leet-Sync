class Solution:
    def trapRainWater(self, nums: List[List[int]]) -> int:

        n=len(nums)
        m=len(nums[0])

        import heapq

        heap=[]
        visited=set()
        for i in range(n):
            for j in range(m):
             if i==0 or i==n-1 or j==0 or j==m-1:
                heapq.heappush(heap,(nums[i][j],i,j))
                visited.add((i,j))
        
        ans=0
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
       
        while heap:
            height,i,j=heapq.heappop(heap)

            for x,y in dirs:
                nx=i+x
                ny=j+y

                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    if height>nums[nx][ny]:
                        ans+=height-nums[nx][ny]
                    heapq.heappush(heap,(max(height,nums[nx][ny]),nx,ny))
        return ans

        

        
        

        
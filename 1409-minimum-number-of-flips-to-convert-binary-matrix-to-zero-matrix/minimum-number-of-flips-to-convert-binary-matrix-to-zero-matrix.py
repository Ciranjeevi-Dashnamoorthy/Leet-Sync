class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        
        from collections import deque

        m,n=len(mat),len(mat[0])

        start=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    start |= (1<<(i*n + j))
        queue=deque([(start,0)])
        vis=set()
        vis.add(start)
        dirs=[(0,0),(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            curr,steps=queue.popleft()
            if curr==0:
                return steps

            for r in range(m):
                for c in range(n):
                    new=curr
                    for i,j in dirs:
                        nr,nc=r+i,j+c

                        if 0<=nr<m and 0<=nc<n:
                            new^=(1<<(nr*n+nc))
                    if new not in vis:
                        vis.add(new)
                        queue.append((new,steps+1))
        return -1



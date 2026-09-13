class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n=len(img1)
        ans=0
        for dx in range(-n+1,n):
            for dy in range(-n+1,n):
                curr=0
                for r in range(n):
                    for c in range(n):

                        nr=r+dx
                        nc=c+dy

                        if 0<=nr< n and 0<=nc<n:
                            if img1[r][c]==1 and img2[nr][nc]==1:
                                curr+=1
                ans=max(ans,curr)
        return ans




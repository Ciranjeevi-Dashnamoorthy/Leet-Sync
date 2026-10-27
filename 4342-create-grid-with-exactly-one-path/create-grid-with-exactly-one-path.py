class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        res=[["#"]*n for _ in range(m)]
        for i in range(n):
            res[0][i]="."
        for i in range(m):
            res[i][n-1]="."

        ans=[]
        for i in res:
            ans.append("".join(i))
        return ans
        
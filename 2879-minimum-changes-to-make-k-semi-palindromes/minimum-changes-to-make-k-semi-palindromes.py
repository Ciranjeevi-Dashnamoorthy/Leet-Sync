class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        mncost = [[inf] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                l = j - i + 1
                for d in range(1, l):
                    if l % d != 0: continue
                    group = l // d
                    curr = 0
                    for start in range(d):
                        for ii in range(group // 2):
                            if s[i + start + ii * d] != s[i + start + (group - 1 - ii) * d]: curr += 1
                    mncost[i][j] = min(mncost[i][j], curr)

        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                for prev in range(i - 1):
                    if dp[prev][j - 1] == inf or mncost[prev][i - 1] == inf: continue
                    dp[i][j] = min(dp[i][j], dp[prev][j - 1] + mncost[prev][i - 1])
        return dp[n][k]








































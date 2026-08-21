class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        m = 1 << n
        bits = [0] * m
        lcm = [0] * m

        for mask in range(1, m):
            clcm = 1
            for i, c in enumerate(coins):
                if mask & (1 << i):
                    clcm = (clcm * c) // gcd(clcm, c)
                    bits[mask] += 1
            lcm[mask] = clcm
        
        def count(x):
            res = 0
            for mask in range(1, m):
                if bits[mask] % 2 == 1: res += x // lcm[mask]
                else: res -= x // lcm[mask]
            return res
        
        l = k
        r = k * min(coins)
        while l < r:
            mid = l + (r - l) // 2
            if count(mid) >= k: r = mid
            else: l = mid + 1
        
        return r

































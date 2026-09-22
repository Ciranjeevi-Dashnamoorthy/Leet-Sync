class ST:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.st = [[0] * (k + 1) for _ in range(self.n * 4)]
        self.build(1, 0, self.n - 1, nums, k)
    
    def merge(self, line1, line2, k):
        newl = line1[::]
        newl[k] = (line1[k] * line2[k]) % k
        for r in range(k): newl[(r * line1[k]) % k] += line2[r]
        return newl
    
    def build(self, node, l, r, nums, k):
        if l == r:
            r = nums[l] % k
            self.st[node][r] = 1
            self.st[node][k] = r
            return self.st[node]
        
        mid = l + (r - l) // 2
        lc = self.build(node * 2, l, mid, nums, k)
        rc = self.build(node * 2 + 1, mid + 1, r, nums, k)
        self.st[node] = self.merge(lc, rc, k)
        return self.st[node]
    
    def update(self, node, l, r, i, val, k):
        if l == r:
            self.st[node] = [0] * (k + 1)
            r = val % k
            self.st[node][r] = 1
            self.st[node][k] = r
            return self.st[node]
        
        mid = l + (r - l) // 2
        if i <= mid: self.update(node * 2, l, mid, i, val, k)
        else: self.update(node * 2 + 1, mid + 1, r, i, val, k)
        self.st[node] = self.merge(self.st[node * 2], self.st[node * 2 + 1], k)
        return self.st[node]
    
    def query(self, node, l, r, ql, qr, k):
        if l >= ql and r <= qr: return self.st[node]
        if l > qr or r < ql: 
            line = [0] * (k + 1)
            line[k] = 1 % k
            return line

        mid = l + (r - l) // 2
        lc = self.query(node * 2, l, mid, ql, qr, k)
        rc = self.query(node * 2 + 1, mid + 1, r, ql, qr, k)
        return self.merge(lc, rc, k)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = ST(nums, k)
        res = []

        for i, val, start, x in queries:
            st.update(1, 0, n - 1, i, val, k)
            line = st.query(1, 0, n - 1, start, n - 1, k)
            res.append(line[x])
        
        return res





























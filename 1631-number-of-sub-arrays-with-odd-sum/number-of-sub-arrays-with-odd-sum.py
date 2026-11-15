class Solution:
    def numOfSubarrays(self, arr):
        res, even, odd, mod = 0, 0, 0, 10**9 + 7

        for i in range(len(arr) - 1, -1, -1):  # Iterate from the end to the beginning
            if arr[i] % 2 == 1:  # Odd number
                even, odd = odd, (even + 1) % mod
            else:  # Even number
                even = (even + 1) % mod
            
            res = (res + odd) % mod
        
        return res
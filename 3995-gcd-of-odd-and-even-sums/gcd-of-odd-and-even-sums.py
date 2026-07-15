class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        even=0
        for i in range(2,n*2+2,2):
            even+=i
        odd=even-n
        return gcd(even,odd)

        
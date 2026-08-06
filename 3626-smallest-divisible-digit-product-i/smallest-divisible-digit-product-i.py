class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for num in range(n,n+11):
            curr=num
            product=1

            while curr>0:
                digit=curr%10
                product*=digit
                curr//=10

            if product%t==0:
                return num
        



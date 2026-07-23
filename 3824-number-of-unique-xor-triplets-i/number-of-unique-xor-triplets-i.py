class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        """
        Observation:

        think of maxi number we can generate 

        mini is 0 and maxi is based on the maximum bit lentgh

        if the bit lentght is 3
        then we can generate 111 at max which is seven including zero which is 8 --> 2** bit_length
        """
        n=len(nums)
        if n<=2:
            return n
        
        ans=bin(n)[2:]
        return 2**len(ans)
        
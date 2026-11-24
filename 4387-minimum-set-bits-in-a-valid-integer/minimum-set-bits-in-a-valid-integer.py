class Solution:
    def minSetBits(self, nums: list[int], k: int) -> int:

        maxi=max(nums)
        n=len(nums)
        if maxi==0:
            return -1

        b=maxi.bit_length()

        mask=1<<b-1
        subm=[False]*(1<<b)

        count=[0]*b
        cur=0

        for i in range(n):
            num=nums[i]
            for bit in range(b):
                if (num>>bit)&1:
                    count[bit]+=1
                    if count[bit]==k:
                        cur|=1<<bit
            
            if i>=k:
                out=nums[i-k]
                for bit in range(b):

                    if (out>>bit)&1:
                        
                        if count[bit]==k:
                            cur^=1<<bit
                        count[bit]-=1
            if i>=k-1:
                if cur==0:
                    return -1
                subm[cur]=True
        for bi in range(b):
            bit=1<<bi
            for mask in range(1<<b):
                if (mask&bit) and subm[mask^bit]:
                    subm[mask]=True
        ans=0
        for m in range(1<<b):
            if not subm[m]:
                curr=m.bit_count()
                if curr>ans:
                    ans=curr 
        return b-ans
            



        
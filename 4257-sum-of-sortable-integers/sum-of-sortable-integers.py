class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:

        n=len(nums)
        div=[]
        
        for i in range(1,n//2+1):
            if n%i==0:
                div.append(i)
        div.append(n)
        print(div)
        ans=0
        for p in range(1,len(div)):
            k=div[p]
            curr=0
            ct=0
            fl=True
            start=0
            prev_max=0
            curr_max=0
            for i in range(n):
                if nums[i]<prev_max:
                    fl=False
                    break
                curr_max=max(curr_max,nums[i])
                if nums[i]>nums[start+(i+1)%k]:
                    ct+=1
                    if ct>1:
                        fl=False
                        break 
                curr+=1
            
                if curr==k:
                    curr=0
                    start=i+1
                    ct=0
                    prev_max=curr_max
            if fl:
                ans+=k
        actual=sorted(nums)
        if actual==nums:
            ans+=1
        return ans

                


        
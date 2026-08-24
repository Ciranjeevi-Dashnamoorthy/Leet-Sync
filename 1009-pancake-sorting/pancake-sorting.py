class Solution:
    def pancakeSort(self, nums: List[int]) -> List[int]:

        res=[]
        n=len(nums)
        curr=n
        
        for i in range(n-1,-1,-1):
            print(i)
            if nums[i]!=curr:
                idx=0
                for j in range(0,i):
                    if nums[j]==curr:
                        idx=j+1
                res.append(idx)
                res.append(curr)
                new=nums[::]
                print(new)
                new[0:idx]=new[0:idx][::-1]
                print(new)
                new=new[:curr][::-1]
                print(new)
                nums=new[::]
            curr-=1
        return res

        
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n=len(nums)
        res=[]
        for i in range(n):
            res.append([nums[i],i])
        res.sort()
        val=[res[0][0]]
        idx=[res[0][1]]
        print(res)
        
        for i in range(n-1):
            if res[i+1][0]-res[i][0]<=limit:
                val.append(res[i+1][0])
                idx.append(res[i+1][1])
                
            else:
                idx.sort()
                val.sort()
                # print(idx)
                # print(val)
                for j in range(len(val)):
                    nums[idx[j]]=val[j]
                val=[res[i+1][0]]
                idx=[res[i+1][1]]
        #     print(val)
        #     print(idx)
        # print("yes")
        idx.sort()
        val.sort()
        # print(idx)
        # print(val)
        for i in range(len(val)):
            nums[idx[i]]=val[i]
        return nums





            
        return nums


        
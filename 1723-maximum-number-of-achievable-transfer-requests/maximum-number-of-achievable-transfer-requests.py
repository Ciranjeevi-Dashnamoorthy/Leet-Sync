class Solution:
    def maximumRequests(self, n: int, nums: list[list[int]]) -> int:

        m=len(nums)
        check=[0]*n
        self.maxi=0

        def dfs(idx,count):

            if idx==m:
                fl=True
                for i in range(n):
                    if check[i]!=0:
                        fl=False
                        break
                if fl:
                    self.maxi=max(self.maxi,count)
                return 
            
            dfs(idx+1,count)
            check[nums[idx][0]]-=1
            check[nums[idx][1]]+=1

            dfs(idx+1,count+1)

            check[nums[idx][0]]+=1
            check[nums[idx][1]]-=1

        dfs(0,0)
        return self.maxi
        


        
        
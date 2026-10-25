class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:

        n=len(nums)
        check=[False]*n
        nums.sort()
        self.ans=0

        def dfs(path):
            
            if len(path)==n:
                print(path)
                self.ans+=1
                return
            
            for i in range(n):
                if check[i]:
                    continue
                if i>0 and nums[i-1]==nums[i] and not check[i-1]:
                    continue

                if path:
                    val=path[-1]+nums[i]
                    sqrt=val**0.5
                    if int(sqrt)**2==val:
                        path.append(nums[i])
                        check[i]=True
                        dfs(path)
                        path.pop()
                        check[i]=False
                else:
                    check[i]=True
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    check[i]=False
        dfs([])
        return self.ans
                
                



        
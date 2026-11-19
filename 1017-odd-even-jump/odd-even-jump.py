class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        
        n=len(arr)

        def check(arr):
            res=[-1]*n
            stack=[]
            for i in arr:
                while stack and stack[-1]<i[1]:
                    idx=stack.pop()
                    res[idx]=i[1]
                stack.append(i[1])
            return res

        asc=[]
        desc=[]
        for i in range(n):
            asc.append((arr[i],i))
            desc.append((arr[i],i))
        
        asc.sort()
        desc.sort(key = lambda x:(-x[0],x[1]))

        even=[False]*n
        odd=[False]*n 
        high=check(asc)
        low=check(desc)

        even[-1]=True
        odd[-1]=True

        for i in range(n-2,-1,-1):
            if high[i]!=-1:
                odd[i]=even[high[i]]
            if low[i]!=-1:
                even[i]=odd[low[i]]
        return sum(odd)
        
        
        
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n=len(items)

        freq=[0]*(n+1)
        mini=float("inf")
        for f,p in items:
            freq[f]+=1
            if mini>p:
                mini=p
        
        free=[0]*(n+1)
        ans=0

        for i in range(1,n+1):
            if freq[i]:
                mul=0
                for j in range(i,n+1,i):
                    mul+=freq[j]
                free[i]=mul-1
        
        items.sort(key=lambda x:x[1])
        limit=2*mini
        for f,p in items:
            if p>limit or budget<0:
                break 
            cap=free[f]
            if cap>0:
                take=min(cap,budget//p)
                budget-=take*p
                ans+=2*take 
        ans+=(budget//mini)
        return ans
        

        
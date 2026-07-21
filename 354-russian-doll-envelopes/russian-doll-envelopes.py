import bisect
class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:

        arr.sort(key= lambda x: (x[0],-x[1]))

        ans=[]
        ans.append(arr[0][1])

        for w,h in arr:
            
            idx=bisect.bisect_left(ans,h)
            if idx==len(ans):
                ans.append(h)
            else:
                ans[idx]=h
        return len(ans)

            
            
        
        
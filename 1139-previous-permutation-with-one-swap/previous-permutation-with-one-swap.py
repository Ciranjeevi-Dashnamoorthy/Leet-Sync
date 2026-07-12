class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        n=len(arr)
        idx=-1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                idx=i
                break
        if idx==-1:
            return arr
        
        swap=idx
        maxi=0
        for i in range(idx+1,n):
            if arr[idx]>arr[i] :
                if maxi<arr[i]:
                    maxi=arr[i]
                    swap=i
            
        print(idx,swap)
        arr[idx],arr[swap]=arr[swap],arr[idx]
        return arr
            
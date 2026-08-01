class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        
        n=len(arr)
        maxi=1

        left=[1]*n
        for i in range(1,n):
            if arr[i-1]<=arr[i]:
                left[i]=left[i-1]+1
                maxi=max(maxi,left[i])
            else:
                maxi=max(maxi,left[i-1]+1)

                
        
        right=[1]*n
        for i in range(n-2,-1,-1):
            
            if arr[i+1]>=arr[i]:
                right[i]=1+right[i+1]
                maxi=max(maxi,right[i])
            else:
                maxi=max(maxi,right[i+1]+1)
        
        for i in range(1,n-1):

            if arr[i-1]<=arr[i+1]:
                maxi=max(maxi,left[i-1]+right[i+1]+1)

        return maxi


     
                    
                
        
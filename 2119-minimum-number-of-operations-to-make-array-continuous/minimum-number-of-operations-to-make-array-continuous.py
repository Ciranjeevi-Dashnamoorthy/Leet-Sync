class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Dont try to do it in O(n), when you know greedy wont work
        think of bs when you know you cant do it in your way 

        Observation:
        sorting array works
        finding the longest existing sequence and subbing wont work
        brute forcing with optimization works

        choose a point nums[i] target it as a initial point why
        explore all possibilities, think why cant we , Greedy wont work

        after choosing num[i], how much elements we actually have to include it in the array , which is nums[i]+n-1

        so we just want to know how much we already have ithe array 
        bf would be using for loop and checking 
        use binary serach to find how many elements we actuallly have 
        since the array is sorted already

        operations needed = n-(j-i)

        what if duplicates arises , we have to remove them so use set and sort 
        the array

        """

        def search(arr,target):
            n=len(arr)
            i,j=0,n-1
            while i<=j:
                mid=(i+j)//2
                if arr[mid]<=target:
                    i=mid+1
                else:
                    j=mid-1
            return i



        n=len(nums)

        arr=sorted(set(nums))
        mini=n
        print(arr)

        for i in range(len(arr)):

            target=arr[i]+n-1
            # print(target)
            idx=search(arr,target)
            # print(idx-i)
            ops=n-(idx-i)
            mini=min(ops,mini)
            # print()

        return mini

        

        

        
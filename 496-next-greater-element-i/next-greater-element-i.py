class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        m=len(nums1)
        res=[-1]*n
        stack=[]
        idx={}
        for i in range(n):

            while stack and nums2[stack[-1]]<nums2[i]:
                new=stack.pop()
                res[new]=nums2[i]
            idx[nums2[i]]=i
            stack.append(i)
        
        ans=[-1]*m
        for i in range(m):
            ans[i]=res[idx[nums1[i]]]
        return ans

        



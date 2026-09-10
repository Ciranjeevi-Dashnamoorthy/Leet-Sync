# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0

        def dfs(node):
            if not node:
                return 0,0

            ls,lct=dfs(node.left)
            rs,rct=dfs(node.right)

            s=ls+rs+node.val
            count=lct+rct+1

            if (s//count)==node.val:
                self.ans+=1

            return s,count
        
        dfs(root)
        return self.ans
        
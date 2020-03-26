# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0

        def length(r):
            if not r:
                return -1
            left = 1 + length(r.left)
            right = 1 + length(r.right)
            nonlocal ans
            ans = max(ans,left + right)
            return max(left,right)
        
        length(root)
        return ans
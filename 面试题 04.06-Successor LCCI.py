# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None
        while root:
            if root.val > p.val:
                ans = root
                root = root.left
            elif root.val <= p.val:
                root = root.right
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def isLeaf(root):
            if root.left or root.right:
                return False
            return True

        if root.left:
            self.removeLeafNodes(root.left,target)
            if isLeaf(root.left) and root.left.val == target:
                root.left = None
        if root.right:
            self.removeLeafNodes(root.right,target)
            if isLeaf(root.right) and root.right.val == target:
                root.right = None
        if isLeaf(root) and root.val == target:
            return None
        else:
            return root
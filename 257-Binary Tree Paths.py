# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        l = self.binaryTreePaths(root.left)
        r = self.binaryTreePaths(root.right)
        if l or r:
            ans = []
            for v in l + r:
                ans.append(str(root.val) + '->' + v)
            return ans
        else:
            return [str(root.val)]
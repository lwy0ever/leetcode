# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        pos = n // 2
        root = TreeNode(nums[pos])
        root.left = self.sortedArrayToBST(nums[:pos])
        root.right = self.sortedArrayToBST(nums[pos + 1:])
        return root
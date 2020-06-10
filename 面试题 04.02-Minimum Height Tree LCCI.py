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
        if n == 1:
            return TreeNode(nums[0])
        r = TreeNode(nums[n // 2])
        r.left = self.sortedArrayToBST(nums[:n // 2])
        r.right = self.sortedArrayToBST(nums[n // 2 + 1:])
        return r
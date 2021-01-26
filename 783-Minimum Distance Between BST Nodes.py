# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def md(r):  # 返回以r为根的树的最小值,最大值,最小差值
            if not r:
                return float('inf'),float('-inf'),float('inf')
            left = md(r.left)
            right = md(r.right)
            return min(r.val,left[0]),max(r.val,right[1]),min(r.val - left[1],right[0] - r.val,left[2],right[2])
        
        return md(root)[2]
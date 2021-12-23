# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0
        def bst(r,l,h):
            if not r:
                return
            if r.val >= l and r.val <= h:
                #print(self.ans,r.val)
                self.ans += r.val
            if r.val > l:
                bst(r.left,l,h)
            if r.val < h:
                bst(r.right,l,h)
        bst(root,low,high)
        return self.ans
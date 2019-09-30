# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0

        def dc(root):
            if not root:
                return 0
            l = dc(root.left)
            r = dc(root.right)
            self.ans += abs(l) + abs(r)
            return root.val + l + r - 1
        
        dc(root)
        return self.ans
                
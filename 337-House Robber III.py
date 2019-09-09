# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if root:
                l1,l2 = dfs(root.left)
                r1,r2 = dfs(root.right)
                r = root.val + l2 + r2
                return max(r,l1 + r1),l1 + r1
            else:
                return 0,0
        ans = dfs(root)
        #print(ans)
        return max(ans)        
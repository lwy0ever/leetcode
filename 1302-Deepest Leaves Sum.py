# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # bfs
        ans = 0
        p = []
        if root:
            p.append(root)
        while p:
            np = []
            ans = 0
            for r in p:
                ans += r.val
                if r.left:
                    np.append(r.left)
                if r.right:
                    np.append(r.right)
            p = np
        return ans
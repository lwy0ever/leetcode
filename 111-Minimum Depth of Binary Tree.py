# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # bfs
        if not root:
            return 0
        ans = 1
        stack = [root]
        while True:
            n_stack = []
            for s in stack:
                if s.left == None and s.right == None:
                    return ans
                if s.left:
                    n_stack.append(s.left)
                if s.right:
                    n_stack.append(s.right)
            stack = n_stack
            ans += 1
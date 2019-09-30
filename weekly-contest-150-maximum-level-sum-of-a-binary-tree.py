# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ans = 1
        ma = root.val
        nodes = [root]
        level = 1
        while nodes:
            newNodes = []
            s = 0
            for n in nodes:
                s += n.val
                if n.left:
                    newNodes.append(n.left)
                if n.right:
                    newNodes.append(n.right)
            if s > ma:
                ma = s
                ans = level
            nodes = newNodes
            level += 1
        return ans
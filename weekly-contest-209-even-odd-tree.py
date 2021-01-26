# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        # bfs
        if not root:
            return True
        if root.val & 1 == 0:
            return False
        level = 0
        nodes = [root]
        while nodes:
            level ^= 1
            newNodes = []
            for n in nodes:
                if n.left:
                    if level:   # 奇数层,需要偶数,且递减
                        if n.left.val & 1 == 0 and (not newNodes or newNodes[-1].val > n.left.val):
                            newNodes.append(n.left)
                        else:
                            return False
                    else:   # 偶数层,需要奇数,且递增
                        if n.left.val & 1 == 1 and (not newNodes or newNodes[-1].val < n.left.val):
                            newNodes.append(n.left)
                        else:
                            return False
                if n.right:
                    if level:   # 奇数层,需要偶数,且递减
                        if n.right.val & 1 == 0 and (not newNodes or newNodes[-1].val > n.right.val):
                            newNodes.append(n.right)
                        else:
                            return False
                    else:   # 偶数层,需要奇数,且递增
                        if n.right.val & 1 == 1 and (not newNodes or newNodes[-1].val < n.right.val):
                            newNodes.append(n.right)
                        else:
                            return False
            nodes = newNodes
        return True
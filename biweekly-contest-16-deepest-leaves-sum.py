# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # bfs
        tns = [root]
        while tns:
            new_tns = []
            for tn in tns:
                if tn.left:
                    new_tns.append(tn.left)
                if tn.right:
                    new_tns.append(tn.right)
            if new_tns:
                tns = new_tns
            else:
                return sum(tn.val for tn in tns)
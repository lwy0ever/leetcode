# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        ans = []
        def p(node,q,formed):   # 当前考虑节点node,未处理的队列为q,已经形成的数组为formed
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not q:
                ans.append(formed)
            for i,nd in enumerate(q):
                # 任取其中一个节点
                newQ = q[:i] + q[i + 1:]
                p(nd,newQ,formed + [nd.val])
        p(root,[],[root.val])
        return ans
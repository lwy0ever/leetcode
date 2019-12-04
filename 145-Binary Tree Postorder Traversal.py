# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 后续遍历=前序遍历的逆序
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            r = stack.pop()
            ans.append(r.val)
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        return ans[::-1]
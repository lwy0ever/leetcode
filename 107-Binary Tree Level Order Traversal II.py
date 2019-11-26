# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            one_ans = []
            n_stack = []
            for s in stack:
                one_ans.append(s.val)
                if s.left:
                    n_stack.append(s.left)
                if s.right:
                    n_stack.append(s.right)
            stack = n_stack
            ans.append(one_ans)
        return ans[::-1]
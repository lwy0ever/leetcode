# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = []
        if root:
            stack.append(root)
        direction = 1   # 1表示先left,后right;0表示先right,后left
        # 本质上是一个bfs
        while stack:
            new_stack = []
            one_ans = []
            while stack:
                s = stack.pop()
                one_ans.append(s.val)
                if direction == 1:
                    if s.left:
                        new_stack.append(s.left)
                    if s.right:
                        new_stack.append(s.right)
                else:
                    if s.right:
                        new_stack.append(s.right)
                    if s.left:
                        new_stack.append(s.left)
            ans.append(one_ans)
            stack = new_stack
            direction ^= 1
        return ans
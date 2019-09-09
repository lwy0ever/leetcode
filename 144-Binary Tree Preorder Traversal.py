# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            n = stack.pop()
            ans.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return ans
        '''
        ans = []
        stack = deque()
        if root:
            stack.append(root)
        while stack:
            n = stack.popleft()
            ans.append(n.val)
            if n.right:
                stack.appendleft(n.right)
            if n.left:
                stack.appendleft(n.left)
        return ans
        '''
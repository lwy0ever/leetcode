# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
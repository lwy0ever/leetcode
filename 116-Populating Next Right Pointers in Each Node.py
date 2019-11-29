"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        l = root.left
        r = root.right
        while l:
            l.next = r
            l = l.right
            r = r.left
        self.connect(root.left)
        self.connect(root.right)
        return root
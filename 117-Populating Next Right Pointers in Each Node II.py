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
    def findchild(self,root):
        #root = root.next
        while root:
            if root.left:
                return root.left
            if root.right:
                return root.right
            root = root.next
        return None
            
    def connect(self, root: 'Node') -> 'Node':
        if root:
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = self.findchild(root.next)
            if root.right:
                root.right.next = self.findchild(root.next)
            self.connect(root.right)
            self.connect(root.left)
        return root
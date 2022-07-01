"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #print(root.children)
        if root:
            return max([0] + [self.maxDepth(child) for child in root.children]) + 1
        else:
            return 0
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans
        stack = [root]
        while stack:
            new_stack = []
            row = []
            for n in stack:
                row.append(n.val)
                for c in n.children:
                    new_stack.append(c)
            ans.append(row)
            stack = new_stack
        return ans
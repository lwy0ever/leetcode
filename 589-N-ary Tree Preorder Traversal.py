"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(r):
            if r:
                ans.append(r.val)
                for c in r.children:
                    dfs(c)
        dfs(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(tns):
            if not tns:
                return
            nonlocal ans
            arr = []
            new_tns = []
            for tn in tns:
                arr.append(tn.val)
                if tn.left:
                    new_tns.append(tn.left)
                if tn.right:
                    new_tns.append(tn.right)
            ans.append(arr)
            bfs(new_tns)
        
        ans = []
        if root:
            bfs([root])
        return ans
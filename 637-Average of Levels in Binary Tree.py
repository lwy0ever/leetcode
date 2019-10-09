# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def bfs(tns):
            if not tns:
                return
            nonlocal ans
            new_tns = []
            arr = []
            for tn in tns:
                arr.append(tn.val)
                if tn.left:
                    new_tns.append(tn.left)
                if tn.right:
                    new_tns.append(tn.right)
            ans.append(sum(arr) / len(arr))
            bfs(new_tns)
        
        ans = []
        bfs([root])
        return ans
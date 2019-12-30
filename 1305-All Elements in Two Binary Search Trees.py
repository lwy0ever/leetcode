# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1 = []
        t2 = []
        def dfs(t,r):
            if not r:
                return
            dfs(t,r.left)
            t.append(r.val)
            dfs(t,r.right)
            
        dfs(t1,root1)
        dfs(t2,root2)
        #print(t1)
        #print(t2)
        
        c1 = 0
        c2 = 0
        ans = []
        while c1 < len(t1) and c2 < len(t2):
            if t1[c1] <= t2[c2]:
                ans.append(t1[c1])
                c1 += 1
            else:
                ans.append(t2[c2])
                c2 += 1
        while c1 < len(t1):
            ans.append(t1[c1])
            c1 += 1
        while c2 < len(t2):
            ans.append(t2[c2])
            c2 += 1
        return ans
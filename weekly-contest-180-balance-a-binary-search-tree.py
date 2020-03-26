# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        def dfs(r):
            if r:
                dfs(r.left)
                self.arr.append(r.val)
                dfs(r.right)
        dfs(root)
        #print(self.arr)
        n = len(self.arr)
        #print(n)
        def cons(root,l,m,r):
            if l < m:
                root.left = TreeNode(self.arr[(l + m) // 2])
                cons(root.left,l,(l + m) // 2,m)
            if m + 1 < r:
                root.right = TreeNode(self.arr[(m + 1 + r) // 2])
                cons(root.right,m + 1,(m + 1 + r) // 2,r)
        r = TreeNode(self.arr[n // 2])
        cons(r,0,n // 2,n)
        #print(r)
        return r
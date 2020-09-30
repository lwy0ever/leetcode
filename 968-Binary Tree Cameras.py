# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 对于节点r,返回3种情况需要的摄像头数量
        # 1,在节点r本身放置摄像头(同时可以兼顾其父节点),所需要的最少摄像头数量
        # 2,节点r本身可以放置也可以不放置摄像头,满足r及子节点都覆盖的情况下,所需要的最少摄像头数量
        # 3,节点r本身可以不被监控(节点r可能不被覆盖),两个子树被监控所需要的摄像头总和
        # 情况1 >= 情况2 >= 情况3
        def dfs(r):
            if not r:
                return float('inf'),0,0 # 情况1=float('inf'),是因为不可能实现在r放置摄像头的情况
            lA,lB,lC = dfs(r.left)
            rA,rB,rC = dfs(r.right)
            # 在r添加摄像头,r.left和r.right可以不用摄像头
            a = lC + rC + 1
            # 3种情况
            # r放
            # r.left放,r.right随意
            # r.left随意,r.right放
            b = min(a,lA + rB,lB + rA)
            # 2种情况
            # r放置摄像头,协助监控r.left和r.right
            # r不放置摄像头
            c = min(a,lB + rB)
            return a,b,c
        
        a,b,c = dfs(root)
        return b
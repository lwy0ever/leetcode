# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # 广度优先搜索
        if not root or root.val in (x,y):
            return False
        nodeList = [(root,0)]   # 记录结点和结点的父结点值
        while nodeList:
            newList = []
            founded = 0
            father = 0
            for n,f in nodeList:
                if n.val in (x,y):
                    if founded == 0:
                        founded += 1
                        father = f
                    else:   # founded = 1
                        return father != f
                if n.left:
                    newList.append((n.left,n.val))
                if n.right:
                    newList.append((n.right,n.val))
            nodeList = newList
            #print([(n.val,f) for n,f in nodeList])
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 需要记录每个节点的父节点
        father = dict()
        # bfs记录父节点
        fromP = {root}
        # 顺便找target节点
        targetNode = None
        while fromP:
            toP = set()
            for f in fromP:
                if f.val == target.val: # 顺便找target节点
                    targetNode = f
                if f.left:
                    father[f.left.val] = f
                    toP.add(f.left)
                if f.right:
                    father[f.right.val] = f
                    toP.add(f.right)
            fromP = toP
            #print(fromP)
        #print(father)
        
        # bfs找距离k的节点
        fromP = {targetNode}
        #print(targetNode.val)
        visited = {target.val}
        for i in range(k):
            toP = set()
            for f in fromP:
                if f.left and f.left.val not in visited:
                    toP.add(f.left)
                    visited.add(f.left.val)
                if f.right and f.right.val not in visited:
                    toP.add(f.right)
                    visited.add(f.right.val)
                if f.val in father and father[f.val].val not in visited:
                    toP.add(father[f.val])
                    visited.add(father[f.val].val)
            fromP = toP
            #print([f.val for f in fromP])
        ans = [f.val for f in fromP]
        return ans
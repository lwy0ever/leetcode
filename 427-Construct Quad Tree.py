"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x,y,length): # 表示grid[x][y]为最上角,长度为length的正方形的四叉树表示
            if length > 1:
                l = length // 2
                tl = helper(x,y,l)
                tr = helper(x,y + l,l)
                bl = helper(x + l,y,l)
                br = helper(x + l,y + l,l)
                if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
                    if tl.val == tr.val == bl.val == br.val:
                        return Node(tl.val,True,None,None,None,None)
                return Node(1,False,tl,tr,bl,br)
            else:
                return Node(grid[x][y],True,None,None,None,None)

        n = len(grid)
        return helper(0,0,n)
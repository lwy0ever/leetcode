# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        valuePos = dict()
        # 提前存储数值在inorder中的位置(数值唯一)
        for i in range(n):
            valuePos[inorder[i]] = i
        
        def r(p1,p2,l): # p1表示preorder的起始位置,p2表示inorder的起始位置,l表示需要考虑的长度
            #print(p1,p2,l)
            if l == 0:
                return None
            node = TreeNode(preorder[p1])
            pos = valuePos[preorder[p1]]
            #print(pos)
            node.left = r(p1 + 1,p2,pos - p2)
            node.right = r(p1 + 1 + pos - p2,pos + 1,l - (pos - p2) - 1)
            return node
        return r(0,0,n)
            
        # 下面的方法需要多次在数组中查找,而且生成多个新数组,时间和空间效率都比较低
        '''
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:pos + 1],inorder[:pos])
        node.right = self.buildTree(preorder[pos + 1:],inorder[pos + 1:])
        return node
        '''
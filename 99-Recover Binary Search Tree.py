# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 对二叉搜索树进行中序遍历(中序遍历:left -> root -> right)
        # 对于遍历的结果序列A,当i < j时,A[i] < A[j]
        # 当A[x]和A[y]发生交换(x < y),则A[x] > A[x + 1],A[y - 1] > A[y]
        # 由此可以确定x和y
        self.nodeX = None
        self.nodeY = None
        self.preNode = TreeNode(float('-inf'))
        
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            #print(root.val,self.nodeX,self.nodeY,self.preNode.val)
            if self.nodeX == None:   # 先找x
                if self.preNode.val > root.val:
                    self.nodeX = self.preNode
            # 如果已经找到了x,再找y
            # 有可能x + 1 = y,所以x和y有可能同时找到,因此这里不能用else
            if self.nodeX:
                if self.preNode.val > root.val:
                    self.nodeY = root
                    #return  # x,y都找到了,但是有可能是x + 1 = y的情况,需要找到最后一个y
            self.preNode = root
            #print(root.val,self.nodeX,self.nodeY,self.preNode.val)
            in_order(root.right)
            
        in_order(root)
        self.nodeX.val,self.nodeY.val = self.nodeY.val,self.nodeX.val
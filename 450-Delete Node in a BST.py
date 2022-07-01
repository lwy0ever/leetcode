# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1,先找到要删除的节点
        # 2,如果节点无子节点,则直接删除
        # 3,如果有子节点,将左子树的最右点or右子树的最左点,赋值到当前节点,并删除最右or左节点
        
        def findLeftMax(tn): # 返回子树的最大值(最右侧节点)
            while tn.right:
                tn = tn.right
            return tn.val            
            
        def findRightMin(tn):    # 返回子树的最小值(最左侧节点)
            while tn.left:
                tn = tn.left
            return tn.val
        
        if not root:
            return None
        t = root.val
        if root.val == key:
            if root.left:
                root.val = findLeftMax(root.left)   # 返回左子树的最大值(最右侧节点)
                root.left = self.deleteNode(root.left,root.val) # 删除左子树的最大值
            elif root.right:
                root.val = findRightMin(root.right) # 返回右子树的最小值(最左侧节点)
                root.right = self.deleteNode(root.right,root.val)   # 删除右子树的最小值
            else:   # 没有子节点
                root = None # 自宫
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)  # 删除左子树的key值
        else:   # root.val < key
            root.right = self.deleteNode(root.right,key)    # 删除右子树的key值
        #print(t,root.val)
        return root
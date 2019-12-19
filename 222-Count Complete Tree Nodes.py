# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def countLeftLevel(root):   # 计算子树的左侧深度
            cnt = 0
            while root:
                root = root.left
                cnt += 1
            return cnt
        
        def countNodesWithLevel(root,n):
            if not root:
                return 0
            leftLevel = n
            rightLevel = countLeftLevel(root.right)
            if leftLevel == rightLevel: # 左右子树的左侧深度相等,说明左子树是满树
                return (1 << leftLevel) + self.countNodes(root.right)
            else:   # 说明左子树不是满树,右子树是满树
                return (1 << rightLevel) + self.countNodes(root.left)            
        
        leftLevel = countLeftLevel(root.left)
        rightLevel = countLeftLevel(root.right)
        # 深度为level的满树,结点数 = 2 ^ level - 1
        # 加上root结点,刚好是2 ^ level,也就是1 << level
        if leftLevel == rightLevel: # 左右子树的左侧深度相等,说明左子树是满树
            return (1 << leftLevel) + countNodesWithLevel(root.right,rightLevel - 1)
        else:   # 说明左子树不是满树,右子树是满树
            return (1 << rightLevel) + countNodesWithLevel(root.left,leftLevel - 1)
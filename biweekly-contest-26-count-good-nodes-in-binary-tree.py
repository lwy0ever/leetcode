# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 1    # 由于节点数据大于等于1,根节点一定存在,根节点必然是好节点
        
        def check(node,_max):
            if node.val >= _max:
                self.ans += 1
                #print(node.val)
            if node.left:
                check(node.left,max(_max,node.val))
            if node.right:
                check(node.right,max(_max,node.val))
            
        if root.left:
            check(root.left,root.val)
        if root.right:
            check(root.right,root.val)
        return self.ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                return 'None,'
            return str(root.val) + ',' + dfs(root.left) + dfs(root.right)
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            tn = TreeNode(l[0])
            l.pop(0)
            tn.left = dfs(l)
            tn.right = dfs(l)
            return tn
        
        l = data.split(',')
        return dfs(l)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
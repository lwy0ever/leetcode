# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(tn):
            if tn:
                return postorder(tn.left) + postorder(tn.right) + [tn.val]
            else:
                return []
        return ' '.join(map(str,postorder(root)))
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def d(arr,_min,_max):
            if arr and _min < arr[-1] < _max:
                tn = TreeNode(arr.pop())
                tn.right = d(arr,tn.val,_max)
                tn.left = d(arr,_min,tn.val)
                return tn
            else:
                return None
        arr = list(map(int,data.split()))
        return d(arr,float('-inf'),float('inf'))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.empty = list() # 记录所有未完全填充的节点
        cur = [root]
        while cur:
            c = cur.pop(0)
            if not c.left or not c.right:
                self.empty.append(c)
            if c.left:
                cur.append(c.left)
            if c.right:
                cur.append(c.right)

    def insert(self, val: int) -> int:
        tn = TreeNode(val)
        e = self.empty[0]
        if e.left:
            e.right = tn
            self.empty.pop(0)
        else:
            e.left = tn
        self.empty.append(tn)
        return e.val

    def get_root(self) -> TreeNode:
        return self.root



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
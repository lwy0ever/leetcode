# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.empty = []
        cur = [root]
        while cur:
            new_cur = []
            for c in cur:
                if not c.left or not c.right:
                    self.empty.append(c)
                if c.left:
                    new_cur.append(c.left)
                if c.right:
                    new_cur.append(c.right)
            cur = new_cur

    def insert(self, v: int) -> int:
        #print(self.empty)
        tn = TreeNode(v)
        p = self.empty[0]
        if not p.left:
            p.left = tn
        else:
            p.right = tn
            self.empty.pop(0)
        self.empty.append(tn)
        return p.val
       

    def get_root(self) -> TreeNode:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
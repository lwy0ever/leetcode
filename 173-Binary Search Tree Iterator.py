# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []   # 标记节点
        r = root
        while r:
            self.stack.append(r)
            r = r.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        t = self.stack[-1]
        r = self.stack.pop()
        r = r.right
        while r:
            self.stack.append(r)
            r = r.left
        return t.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
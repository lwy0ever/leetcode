# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        #self.stack = []
        #bisect.insort(self.stack,0)
        root.val = 0
        def rebuild(tn):
            if tn.left:
                tn.left.val = tn.val * 2 + 1
                #bisect.insort(self.stack,tn.left.val)
                rebuild(tn.left)
            if tn.right:
                tn.right.val = tn.val * 2 + 2
                #bisect.insort(self.stack,tn.right.val)
                rebuild(tn.right)
        rebuild(root)
        self.root = root
        #print(self.stack)

    def find(self, target: int) -> bool:
        if target < 0:
            return False
        t = bin(target + 1)
        i = 3
        n = len(t)
        cur = self.root
        while i < n:
            if t[i] == '0':
                if cur.left:
                    cur = cur.left
                else:
                    return False
            else:
                if cur.right:
                    cur = cur.right
                else:
                    return False
            i += 1
        return True
        '''
        pos = bisect.bisect_right(self.stack,target)
        if self.stack[pos - 1] == target:
            return True
        else:
            return False
        '''

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
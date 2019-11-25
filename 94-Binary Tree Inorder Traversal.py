# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
        '''
        ans = []
        stack = [] # stack[i]存储[节点,状态],状态0表示未遍历左侧,状态1表示已遍历左侧
        if root:
            stack.append([root,0])
        while stack:
            #print(stack)
            if stack[-1][1] == 0:
                stack[-1][1] = 1
                if stack[-1][0].left:
                    stack.append([stack[-1][0].left,0])
            else:
                t,_ = stack.pop()
                ans.append(t.val)
                if t.right:
                    stack.append([t.right,0])
        return ans
        '''
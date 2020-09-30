"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 基础思路:宽度优先搜索,空间复杂度O(N)
        '''
        if not root:
            return root
        q = []
        level = 0
        q.append((root,level))
        i = 0
        while i < len(q):
            node = q[i][0]
            l = q[i][1]
            if node.left:
                q.append((node.left,l + 1))
            if node.right:
                q.append((node.right,l + 1))
            if i + 1 < len(q):
                if q[i + 1][1] == l:
                    node.next = q[i + 1][0]
            i += 1
        return root
        '''
        # 进阶思路:node.next形成了链表,可以利用其进行宽度优先搜索
        def findChild(node):    # 找到下一层的可用子节点
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            return None
        if root:
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = findChild(root.next)
            if root.right:
                root.right.next = findChild(root.next)
            # 先连接右侧,后连接左侧,避免左右之间空挡
            self.connect(root.right)
            self.connect(root.left)
        return root
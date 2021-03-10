# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 优化遍历方式的分治算法
        # 利用全局变量优化遍历方式
        def getLength(r):
            l = 0
            while r:
                l += 1
                r = r.next
            return l

        def buildTree(left,right):  # 链表的起止位置,返回树的头部
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode()
            root.left = buildTree(left,mid - 1)
            nonlocal head   # 全局变量
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1,right)
            return root

        length = getLength(head)
        return buildTree(0,length - 1)

    # 分治算法
    '''
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findMid(head):
            pre = None  # 为便于切断链表
            slow = head
            fast = head

            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            if pre: # 切断链表
                pre.next = None

            return slow

        if not head:
            return None
        mid = findMid(head)
        root = TreeNode(mid.val)
        if head == mid:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    '''
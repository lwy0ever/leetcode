# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # 用stack存储node
        stack = []
        c = head
        while c:
            stack.append(c)
            c = c.next
        n = (len(stack) - 1) // 2
        c = head
        for i in range(n):
            tail = stack.pop()
            tail.next = c.next
            c.next = tail
            c = tail.next
        stack.pop().next = None
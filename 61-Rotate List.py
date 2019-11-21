# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n = 1   # 列表长度
        c = head
        while c.next:
            c = c.next
            n += 1
        l = n - (k % n)
        c.next = head
        c = head
        for i in range(l - 1):
            c = c.next
        head = c.next
        c.next = None
        return head
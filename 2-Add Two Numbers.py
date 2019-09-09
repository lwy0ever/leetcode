# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        r = cur
        add1 = 0
        while l1 and l2:
            add1,v = divmod(l1.val + l2.val + add1,10)
            n = ListNode(v)
            cur.next = n
            cur = n
            l1 = l1.next
            l2 = l2.next
        while l1:
            add1,v = divmod(l1.val + add1,10)
            n = ListNode(v)
            cur.next = n
            cur = n
            l1 = l1.next
        while l2:
            add1,v = divmod(l2.val + add1,10)
            n = ListNode(v)
            cur.next = n
            cur = n
            l2 = l2.next
        if add1:
            n = ListNode(add1)
            cur.next = n
        return r.next
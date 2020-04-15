# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        added = 0
        head = ListNode(0)
        cur = head
        while l1 or l2 or added:
            t = added
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            added,t = divmod(t,10)
            cur.next = ListNode(t)
            cur = cur.next
        return head.next
            
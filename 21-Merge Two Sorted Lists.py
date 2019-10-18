# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        hh = ListNode(0)
        c = hh
        while l1 and l2:
            if l1.val <= l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        if l1:
            c.next = l1
        else:
            c.next = l2
        return hh.next
        
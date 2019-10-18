# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        hh = ListNode(0)
        c = hh
        h = head
        while h and h.next:
            c.next = h.next
            c = h
            t = h.next.next
            h.next.next = h
            h.next = t
            h = t
            #print(hh,h)
        if h:
            c.next = h
        return hh.next
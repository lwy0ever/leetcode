# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = head
        r = head
        for _ in range(n):
            r = r.next
        if not r: # len(list) == n
            return l.next
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head
        
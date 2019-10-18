# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        hh = ListNode(0)
        hh.next = head
        c = hh
        b = head
        while True:
            # check if the number of nodes is a multiple of k
            checkCur = b
            for _ in range(k):
                if not checkCur:
                    return hh.next
                    break
                checkCur = checkCur.next
            # reverse it
            tail = b
            a = b
            b = a.next
            for _ in range(k - 1):
                tmp = b.next
                b.next = a
                a = b
                b = tmp
            c.next = a
            tail.next = b
            c = tail
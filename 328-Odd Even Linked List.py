# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        evenHead = head.next
        even = evenHead
        while True:
            if even.next:
                odd.next = even.next
                odd = odd.next
            else:
                #odd.next = None
                break
            if odd.next:
                even.next = odd.next
                even = even.next
            else:
                even.next = None
                break
        odd.next = evenHead
        return head
        
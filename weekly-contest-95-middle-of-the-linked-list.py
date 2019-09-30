# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid = head
        tail = head
        cnt = 0
        while tail:
            tail = tail.next
            cnt ^= 1
            if cnt == 0:
                mid = mid.next
        return mid
        
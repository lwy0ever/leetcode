# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        left = head
        right = head
        for i in range(k):
            right = right.next
        while right:
            left = left.next
            right = right.next
        return left.val
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = head
        right = head
        while right:
            if right.val < x:
                left.val,right.val = right.val,left.val
                left = left.next
            right = right.next
        return head
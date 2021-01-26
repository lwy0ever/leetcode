# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curA = list1
        for i in range(a - 1):
            curA = curA.next
        curB = curA.next
        for i in range(b - a + 1):
            curB = curB.next
        curA.next = list2
        while curA.next:
            curA = curA.next
        curA.next = curB
        return list1
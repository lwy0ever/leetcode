# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        existed = set()
        existed.add(head.val)
        pre = head
        cur = head.next
        while cur:
            if cur.val in existed:
                cur = cur.next
                pre.next = cur
            else:
                existed.add(cur.val)
                pre = pre.next
                cur = cur.next
        return head
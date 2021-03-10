# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        
        needMore = True
        while needMore:
            needMore = False
            s = 0
            cur = pre
            val_pos = {}
            while cur:
                s += cur.val
                if s in val_pos:
                    val_pos[s].next = cur.next
                    needMore = True
                else:
                    val_pos[s] = cur
                cur = cur.next
        return pre.next     
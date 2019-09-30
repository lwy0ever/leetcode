# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        
        s = 0
        cur = pre
        val_pos = {}
        while cur:
            s += cur.val
            if s in val_pos:
                val_pos[s].next = cur.next
            else:
                val_pos[s] = cur
            cur = cur.next
        return pre.next
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
        '''
        ans = ListNode(0)
        ans.next = head
        cur = ans
        while cur:
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
        return ans.next
        '''
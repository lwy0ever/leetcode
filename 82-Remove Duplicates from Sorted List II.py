# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        ans.next = head
        cur = ans
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                t = cur.next.val
                while cur.next and cur.next.val == t:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return ans.next
        '''
        ans = ListNode(0)
        c = ans
        cur = head
        while cur:
            if cur.next:
                if cur.val == cur.next.val:
                    #print(cur)
                    while cur.next and cur.val == cur.next.val:
                        cur.next = cur.next.next
                    c.next = None
                    #print(cur)
                else:
                    c.next = cur
                    c = c.next
            else:
                c.next = cur
                c = c.next
            cur = cur.next
        return ans.next
        '''
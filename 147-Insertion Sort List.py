# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        def insert(cur):
            nonlocal head
            h = head
            if cur.val < h.val:
                cur.next = h
                return cur
            while h.next:
                if h.next.val < cur.val:
                    h = h.next
                else:
                    cur.next = h.next
                    h.next = cur
                    return head
            h.next = cur
            cur.next = None
            return head

        toInsert = head.next
        head.next = None
        while toInsert:
            nxt = toInsert.next
            head = insert(toInsert)
            toInsert = nxt
            #print(head)
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hh = ListNode(0)
        val = []
        valCur = []
        for i,ln in enumerate(lists):
            if ln:
                cur = bisect.bisect(val,ln.val)
                bisect.insort(val,ln.val)
                valCur.insert(cur,ln)
        c = hh
        while valCur:
            ln = valCur.pop(0)
            val.pop(0)
            c.next = ln
            if ln.next:
                cur = bisect.bisect(val,ln.next.val)
                bisect.insort(val,ln.next.val)
                valCur.insert(cur,ln.next)
            c = c.next
        return hh.next
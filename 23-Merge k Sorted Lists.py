# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hh = ListNode(0)
        val = []    # 存储值
        valCur = [] # 存储值对应的链表序号
        for i,ln in enumerate(lists):   # 将链表的第一个值排序,插入val中
            if ln:
                cur = bisect.bisect(val,ln.val)
                bisect.insort(val,ln.val)
                valCur.insert(cur,ln)
        c = hh
        while valCur:
            ln = valCur.pop(0)  # 将最小值加入新列表
            val.pop(0)
            c.next = ln
            if ln.next: # 将最小值对应的链表的下一个值插入val
                cur = bisect.bisect(val,ln.next.val)
                bisect.insort(val,ln.next.val)
                valCur.insert(cur,ln.next)
            c = c.next
        return hh.next
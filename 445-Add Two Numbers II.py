# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        #print(s1)
        #print(s2)
        preL = None
        r = (0,0)
        while s1 or s2:
            res = 0
            if s1:
                res += s1.pop()
            if s2:
                res += s2.pop()
            r = divmod(res + r[0],10)
            l = ListNode(r[1])
            l.next = preL
            preL = l
        if r[0] > 0:
            l = ListNode(r[0])
            l.next = preL
        return l
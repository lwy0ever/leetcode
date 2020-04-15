# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 将两个链表连接起来,形成2个链表A+B,B+A,两个链表长度相等
        # 无论从A开始还是从B开始
        # 如果两个链表相交,则末尾若干元素一定相同
        curA = headA
        curB = headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
            if curB:
                curB = curB.next
            else:
                curB = headA
        if curA == None:    # 退出循环是因为curA == curB == None
            return None
        else:   # 退出循环是因为curA == curB != None
            return curA
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def h(cur): # 返回值:是否回文+需要匹配的下一个值
            if cur.next:
                check,t = h(cur.next)
                return check and t.val == cur.val,t.next
            else:
                return cur.val == head.val,head.next
        
        if head:
            return h(head)[0]
        else:
            return True
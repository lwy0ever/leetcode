# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 方法2:
        # 类似快慢指针
        # 让先遣指针指向k + 1
        # 然后先遣指针和普通指针一起后移,当先遣指针指空时停止
        pre = head
        for _ in range(k):
            pre = pre.next
        cur = head
        while pre:
            cur = cur.next
            pre = pre.next
        return cur
        
        # 方法1
        # 先计数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        cur = head
        for _ in range(n - k):
            cur = cur.next
        return cur
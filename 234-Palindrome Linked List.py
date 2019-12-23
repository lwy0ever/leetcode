# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 用快慢指针找到中点
        # 同时将前半部分链表翻转
        if not head or not head.next:
            return True
        rHead = None  # 存储反转后的链表头
        slow = head
        fast = head.next
        while fast and fast.next:
            tmp = slow
            slow = slow.next
            fast = fast.next.next
            # 反转前半部分链表
            tmp.next = rHead
            rHead = tmp
        #print(rHead,slow)
        if fast:    # 说明是偶数个元素,slow指向的是前半部分的尾
            right = slow.next
            slow.next = rHead
            left = slow
        else:   # 说明是奇数个元素,slow指向正中间的元素,不需要判断
            left = rHead
            right = slow.next
        #print(left,right)
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
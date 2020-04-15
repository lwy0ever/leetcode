# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针fast和slow
        # 定义:
        # 从head到环路入口,长度为a
        # 从环路入口到相遇点,长度b
        # 环路长度r
        # 则fast走a + b + (n + 1) * r,同时slow走a + n * r + b,两者相遇
        # a + b + (n + 1) * r = 2 * (a + n * r + b)
        # (n - 1) * r + a + b = 0
        # n * r + a = r - b
        # 也就是a和r - b的差刚好是环路的长度
        # 那么,两者相遇以后,让fast回到head,每次走1步
        # 于是fast走a + x * r,slow走r - b + y * r
        # 两者在入口相遇
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast and fast.next:  # 有环
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        else:   # 没有环
            return None

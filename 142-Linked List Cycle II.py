# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针的方式
        # 如果快指针能够追上慢指针,说明存在cycle
        
        # 指针相遇之后,慢指针不变,新慢指针指向head(新慢指针和原慢指针速度一样)
        # 再次开始移动,则两指针会在cycle的起始点相遇(证明如下)
        # 设从head到cyble的起始点距离为a,起始点到第一次相遇点距离为b,相遇点到起始点距离为c
        # 由于第一次相遇,(a + b) * 2 = a + b + c + b
        # 所以2a + 2b = a + 2b + c
        # 所以a = c,所以两个慢指针会在起始点相遇
        f = head    # f means fast
        s = head    # s means slow
        while True:
            if f and f.next:
                f = f.next.next
                s = s.next
                if f == s:
                    f = head
                    while f != s:
                        f = f.next
                        s = s.next
                    return f
            else:
                return None
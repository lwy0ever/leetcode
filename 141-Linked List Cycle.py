# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针的方式
        # 如果快指针能够追上慢指针,说明存在cycle
        f = head    # f means fast
        s = head    # s means slow
        while True:
            if f and f.next:
                f = f.next.next
                s = s.next
                if f == s:
                    return True
            else:
                return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        if k == 1:
            return [head]
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        ans = [None] * k
        part = n // k
        ext = n % k
        cur = head
        for i in range(k):
            if cur is None:
                break
            ans[i] = cur
            length = part + 1 if ext > 0 else part
            ext -= 1
            for _ in range(length - 1):
                cur = cur.next
            nxt = cur.next
            cur.next = None
            cur = nxt
        return ans
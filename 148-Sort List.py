# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 通过快慢指针找到中点,将其分成2部分
        # 然后模拟进行归并排序
        if not head or not head.next:
            return head
        f = head.next   # f初始化为head.next,是为了让s(slow)能够最终指向中点,而不是中点的后一个点
        s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        # 从中点断开
        mid = s.next
        s.next = None
        # 分别排序
        h1 = self.sortList(head)
        h2 = self.sortList(mid)
        # 归并
        ans = ListNode(0)   # 加一个空头
        cur = ans
        while h1 and h2:
            if h1.val > h2.val:
                cur.next = h2
                h2 = h2.next
            else:
                cur.next = h1
                h1 = h1.next
            cur = cur.next
        if h1:
            cur.next = h1
        else:
            cur.next = h2
        return ans.next
        
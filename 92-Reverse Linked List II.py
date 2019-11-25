# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        ans = ListNode(0)
        ans.next = head
        cur = ans
        i = 0
        preTail = None
        preHead = None
        newHead = None
        newTail = None
        pre = None
        while cur:
            #print(i,cur.val)
            tmp = pre
            pre = cur
            cur = cur.next
            if m <= i <= n:
                pre.next = tmp
                if i == m:
                    preTail = tmp
                    newTail = pre
                elif i == n:
                    newHead = pre
                    preHead = cur
                    break
            i += 1
        #print(preTail.val)
        #print(preHead.val)
        #print(newHead.val)
        #print(newTail.val)
        preTail.next = newHead
        newTail.next = preHead
        return ans.next
        
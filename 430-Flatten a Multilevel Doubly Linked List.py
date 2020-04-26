"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(h):    # 用于处理含有child的节点,返回child的头和尾
            cur = h
            while True:
                if cur.child:
                    n = cur.next
                    newHead,newTail = helper(cur.child)
                    cur.child = None
                    cur.next = newHead
                    newHead.prev = cur
                    if n:
                        n.prev = newTail
                    newTail.next = n
                    cur = newTail
                if cur.next:
                    cur = cur.next
                else:
                    break
            #print(h.val,cur.val)
            return h,cur
        
        if not head:
            return head
        h,_ = helper(head)
        return h
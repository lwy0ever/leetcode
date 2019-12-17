# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归(recursively)
        '''
        if not head or not head.next:
            return head
        def r(head):
            if head.next:
                newhead,tail = r(head.next)
                tail.next = head
                return newhead,head
            else:
                return head,head
        newhead,tail = r(head)
        tail.next = None
        return newhead
        '''

        # 抄的递归
        '''
        # 递归终止条件是当前为空，或者下一个节点为空
        if not head or not head.next:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur
        '''
        
        # 迭代(iteratively)
        # 双指针迭代
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

        # 堆栈
        '''
        if not head:
            return head
        cur = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
        head = stack.pop()
        cur = head
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return head
        '''

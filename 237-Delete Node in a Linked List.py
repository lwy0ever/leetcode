# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node就是链表中的一个节点
        # 如果node是末尾节点,则无法删除,所以题目提到The given node will not be the tail
        # 由于无法获取node的前节点,无法直接用next = next.next来跳过
        # 可以将node.next的值复制给node,然后删除node.next
        node.val = node.next.val
        node.next = node.next.next
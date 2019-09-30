# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans = []
        stack = [] #stack[]=(val,pos)
        i = 0 # 存放当前的pos
        while head:
            ans.append(0) # 存放默认值，当找不到更大结果的时候不需要再处理
            while stack and stack[-1][0] < head.val:
                t = stack.pop()
                ans[t[1]] = head.val
            stack.append((head.val,i))
            head = head.next
            i += 1
        return ans
                
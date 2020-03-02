# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)

        def isp(r,a):
            t = a + [r.val]
            if len(t) >= n:
                ans = True
                for i in range(n):
                    if t[- 1 - i] != arr[- 1 - i]:
                        ans = False
                        break
                if ans:
                    return True
            if r.left and isp(r.left,t):
                return True
            if r.right and isp(r.right,t):
                return True
            return False
        
        return isp(root,[])
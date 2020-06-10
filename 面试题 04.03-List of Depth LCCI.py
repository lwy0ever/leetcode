# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        nodes = [tree]
        while nodes:
            one = ListNode(0)
            cur = one
            newNodes = []
            for n in nodes:
                cur.next = ListNode(n.val)
                cur = cur.next
                if n.left:
                    newNodes.append(n.left)
                if n.right:
                    newNodes.append(n.right)
            ans.append(one.next)
            #print(one,ans)
            nodes = newNodes
        return ans

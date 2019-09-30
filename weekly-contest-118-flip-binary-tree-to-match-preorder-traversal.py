# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        p = 0
        ans = []
        stack = [root]
        n = len(voyage)
        while stack:
            #print(stack,ans)
            node = stack.pop()
            if not node:
                continue
            elif node.val != voyage[p]:
                return [-1]
            #print(voyage[p],node.val,p)
            if node.left and node.right:
                if node.left.val == voyage[p + 1]:
                    stack.append(node.right)
                    stack.append(node.left)
                elif node.right.val == voyage[p + 1]:
                    ans.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    return [-1]
            elif node.left:
                if node.left.val == voyage[p + 1]:
                    stack.append(node.left)
                else:
                    return [-1]
            elif node.right:
                if node.right.val == voyage[p + 1]:
                    stack.append(node.right)
                else:
                    return [-1]
            p += 1
        return ans
                    
                
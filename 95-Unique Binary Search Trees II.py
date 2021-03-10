# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        cache = dict()

        def dfs(left,right):    # 返回[left,right]形成的所有可能的二叉搜索树的根节点列表
            if left > right:
                return [None]   # 返回None,而不是[],是为了保证能够正确的遍历left_tree和right_tree
            if (left,right) in cache:
                return cache[(left,right)]

            ans = []

            for i in range(left,right + 1):
                # all possible left subtrees if i is choosen to be a root
                left_tree = dfs(left,i - 1)
                # all possible right subtrees if i is choosen to be a root
                right_tree = dfs(i + 1,right)
                
                # connect left and right subtrees to the root i
                for l in left_tree:
                    for r in right_tree:
                        tn = TreeNode(i)
                        tn.left = l
                        tn.right = r
                        ans.append(tn)

            cache[(left,right)] = ans
            return ans
        
        return dfs(1,n) if n > 0 else []
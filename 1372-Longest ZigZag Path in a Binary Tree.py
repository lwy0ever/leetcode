# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self._max = 0

        def lzz(r,pre,length):    # pre = 1表示上一个路径向左,-1表示上一个路径向右
            self._max = max(self._max,length)
            if r.right:
                if pre == 1:
                    lzz(r.right,-pre,length + 1)
                else:
                    lzz(r.right,pre,1)
            if r.left:
                if pre == -1:
                    lzz(r.left,-pre,length + 1)
                else:
                    lzz(r.left,pre,1)
        
        lzz(root,1,0)   # 由于length初始化为0,所以pre的值无所谓是1或者-1
        return self._max
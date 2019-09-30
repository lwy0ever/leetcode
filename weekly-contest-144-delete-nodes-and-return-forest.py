# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def cons(self,r,vald):
        if r.left:
            vald[r.left.val] =(r.left,r.val)
            self.cons(r.left,vald)
        if r.right:
            vald[r.right.val] = (r.right,r.val)
            self.cons(r.right,vald)
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        vald = {root.val:(root,-1)}
        self.cons(root,vald)
        #print(vald.keys())
        for d in to_delete:
            #print(vald[vald[d][1]])
            if vald[d][1] == -1:
                f = root
            else:
                if vald[d][1] in vald:
                    v = vald[vald[d][1]]
                    #print(v)
                    f = v[0]
                else:
                    vald.pop(d,0)
                    continue
            if f.left and f.left.val == d:
                f.left = None
            if f.right and f.right.val == d:
                f.right = None
            vald.pop(d,0)
        #print(vald.keys())
        ans = []
        for k in vald.keys():
            if vald[k][1] not in vald:
                #print(vald[k][1])
                ans.append(vald[k][0])
        return ans
        
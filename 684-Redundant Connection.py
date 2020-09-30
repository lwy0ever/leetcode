class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 如果附加了边,则形成环
        n = len(edges)
        # fa[i]表示i的父节点,fa[0]无用
        fa = [i for i in range(n + 1)]
        def findFather(p):
            while fa[p] != p:
                p = fa[p]
            return p
        
        for father,child in edges:
            ff = findFather(father)
            fc = findFather(child)
            if ff == fc:
                return [father,child]
            fa[fc] = ff
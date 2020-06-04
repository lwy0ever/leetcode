class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        ft = collections.defaultdict(list)
        for f,t in edges:
            ft[f].append(t)
        def t(node):
            r = 0
            hasChild = False
            if node in ft:
                for n in ft[node]:
                    r += t(n)
            if hasApple[node] or r > 0:
                r += 1
            return r
        return max(0,(t(0)- 1) * 2)   # 需要去掉根节点,同时需要考虑hasApple全False的情况
        '''
        # 除了根节点,要访问每一个节点,都需要步数+2
        toSee = set()
        for f,t in reversed(edges):
            if hasApple[t] or t in toSee:
                toSee.add(f)
                toSee.add(t)
        toSee.discard(0)
        return 2 * len(toSee)
        '''
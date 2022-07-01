class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 每个edges里面都会有这个节点
        # 简化数据结构
        # 只需要看edges[0],edges[1]就够了
        if edges[1][0] in edges[0]:
            return edges[1][0]
        else:
            return edges[1][1]

        # 使用Counter        
        cnt = collections.Counter()
        for a,b in edges:
            cnt[a] += 1
            if cnt[a] == 2:
                return a
            cnt[b] += 1
            if cnt[b] == 2:
                return b
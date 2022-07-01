class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp + 宽度优先搜索
        # status[(i,j)]表示上一步之后,出现在位置i,j的概率
        status = dict()
        status[(row,column)] = 1.0
        di = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
        for _ in range(k):
            newStatus = collections.defaultdict(int)
            for k,v in status.items():
                i,j = k
                for d in di:
                    ni,nj = i + d[0],j + d[1]
                    if 0 <= ni < n and 0 <= nj < n:
                        newStatus[(ni,nj)] += v / 8
            status = newStatus
        return sum(status.values())
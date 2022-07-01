class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # bfs
        n = len(bombs)
        # di[i]表示boms[i]可以直接引爆的炸弹
        # 然后通过逐个bfs,使之包括可以间接引爆的炸弹
        di = [{i} for i in range(n)]
        # 初始化直接引爆的炸弹
        for i in range(n - 1):
            for j in range(i + 1,n):
                dis = (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                if dis <= bombs[i][2] ** 2:
                    di[i].add(j)
                if dis <= bombs[j][2] ** 2:
                    di[j].add(i)
        #print(di)
        ans = 0
        for i in range(n):
            # bfs
            fromP = list(di[i])
            while fromP:
                toP = set()
                for f in fromP:
                    if f <= i:  # f < i,说明f点已经被考虑过,直接合并,不需要再重新bfs
                        di[i] |= di[f]
                        continue
                    for t in di[f]:
                        if t not in di[i]:
                            di[i].add(t)
                            toP.add(t)
                fromP = toP
            ans = max(ans,len(di[i]))
        return ans
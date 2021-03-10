class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        #if n > sum(rollMax):
        #    return 0
        # d[i][j] 表示出现筛子i,之后剩余j次的情况下,可能的组合数
        d = [[0] * 17 for _ in range(6)]
        ma = [0] * 6    # ma[i]表示筛子i出现的最大次数
        # poss[i] 表示除i以外的可选择种类
        poss = [0] * 6
        for i,j in enumerate(rollMax):
            if j > 0:
                d[i][j] = 1
            ma[i] = j
            for x in range(6):
                if x != i and j > 0:
                    poss[x] += 1
        #print(ma)
        #print(poss)

        for _ in range(n - 1):
            new_poss = [0] * 6
            for i in range(6):
                for j in range(16):
                    if j == ma[i]:
                        d[i][j] = poss[i]
                        for x in range(6):
                            if x != i and j > 0:
                                new_poss[x] += d[i][j]
                        break
                    d[i][j] = d[i][j + 1]
                    for x in range(6):
                        if x != i and j > 0:
                            new_poss[x] += d[i][j]
            poss = new_poss
            #print(d)
            #print(poss)
        ans = 0
        for i in range(6):
            for j in range(1,17):
                ans += d[i][j]
        return ans % (10 ** 9 + 7)
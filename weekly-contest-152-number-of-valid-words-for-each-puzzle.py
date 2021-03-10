class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 状态压缩
        wordStatCnt = collections.Counter()
        base = ord('a')
        for w in words:
            stat = 0
            for c in w:
                stat |= (1 << (ord(c) - base))
            if str(bin(stat)).count('1') <= 7:
                wordStatCnt[stat] += 1
        #print(wordStatCnt)
        n = len(puzzles)
        ans = [0] * n
        for i,p in enumerate(puzzles):
            restStat = 0
            for c in p[1:]:
                restStat |= (1 << (ord(c) - base))
            t = restStat
            while t:
                allStat = t | (1 << (ord(p[0]) - base))
                ans[i] += wordStatCnt[allStat]
                t = (t - 1) & restStat  # 通过这种方式,遍历所有可能性.但是会缺失空集可能性
            # 补空集
            ans[i] += wordStatCnt[1 << (ord(p[0]) - base)]
        return ans

        # 纯copy别人的算法.frozenset和combinations的良好使用
        '''
        d = {}
        for w in words:
            if len(set(w)) <= 7:
                d[frozenset(w)] = d.get(frozenset(w),0) + 1
        ans = []
        for p in puzzles:
            p1 = (p[0],)
            pRest = set(p[1:])
            cnt = 0
            for i in range(len(pRest) + 1):
                for c in itertools.combinations(pRest,i):
                    cnt += d.get(frozenset(c + p1),0)
            ans.append(cnt)
        return ans
        '''
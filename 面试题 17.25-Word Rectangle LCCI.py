class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        # 逐行放置,放置后检查
        preCal = dict()  # preCal[i][s]记录的是单词长度为i的单词,前缀是s的单词的索引位置
        for i,w in enumerate(words):
            n = len(w)
            if n not in preCal:
                preCal[n] = collections.defaultdict(set)
            for l in range(len(w) + 1):
                preCal[n][w[:l]].add(i)
        #print(preCal)
        # maxRect[i] = (l1,l2),表示矩阵面积为i的矩阵,可以由长度l1 x l2获得
        # 考虑矩阵的对角对称性(4x3的=3x4),设定l1 >= l2
        maxRect = collections.defaultdict(list)
        for l1 in preCal.keys():
            for l2 in preCal.keys():
                if l1 < l2:
                    continue
                maxRect[l1 * l2].append((l1,l2))
        #print(maxRect)
        # 计划放置一个totalWidth x totalHeight的矩阵
        # 已经放置了nowHeight行
        def check(rec,totalWidth,totalHeight,nowHeight):
            #print('check',rec,totalWidth,totalHeight,nowHeight)
            for col in range(totalWidth):
                preC = ''.join(rec[i][col] for i in range(nowHeight))
                if preC not in preCal[totalHeight]:
                    return False
            return True
            
        # 尝试宽度totalWidth,高度totalHeight的矩阵
        # 尝试第r行(base0)
        def goTry(totalWidth,totalHeight,r):
            # 每次摆放一行,对列做检查
            # 成功,则尝试下一行
            # 失败,则尝试下一个单词
            # 如果所有单词都失败,则返回失败
            if r == totalHeight:
                return True
            #print('goTry',totalWidth,totalHeight,r)
            preC0 = ''.join(ans[i][0] for i in range(r))
            for iwPreC0 in preCal[totalHeight][preC0]:
                for iwW0 in preCal[totalWidth][words[iwPreC0][r]]:
                    # 尝试words[iwW0]
                    ans.append(words[iwW0])
                    if check(ans,totalWidth,totalHeight,r + 1):
                        if goTry(totalWidth,totalHeight,r + 1):
                            return True
                    ans.pop()
            return False

        ans = []
        for r in sorted(maxRect.keys(),reverse = True):
            for l1,l2 in maxRect[r]:
                if goTry(l1,l2,0):
                    return ans
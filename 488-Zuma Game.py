class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # 按照规则,3个及以上的重复数字都要清理掉
        # 有些情况,比如"R(B)RWWRRBBRR" -> "R(B)RWW(W)RRBBRR" -> ""
        # 需要先插入一个"分隔符"
        # 结论:
        # 1,原则上每次插入,都将字符插入其相邻的字符处,实现剪枝
        # 2,当出现3个以上(其实也就是4个)的连续字符需要消除时,尝试用其他字符将其分成1/3,2/2,3/1三种情况,进行补枝操作
        cache = dict()
        
        def rebuild(b,h):
            while True:
                newB = ''
                ind = 0
                for k,g in itertools.groupby(b):
                    n = len(list(g))
                    if n == 3:
                        continue
                    elif n == 4:
                        # 补枝
                        l = []
                        used = set()
                        l += [[s,ad] for s,ad in rebuild(b[:ind] + b[ind + n:],h)]
                        for i,c in enumerate(h):
                            if c not in used:
                                used.add(c)
                                l += [[s,ad + 1] for s,ad in rebuild(b[:ind + 1] + c + b[ind + 4:],h[:i] + h[i + 1:])]
                                l += [[s,ad + 1] for s,ad in rebuild(b[:ind + 2] + c + b[ind + 2:],h[:i] + h[i + 1:])]
                                l += [[s,ad + 1] for s,ad in rebuild(b[:ind] + c + b[ind + 3:],h[:i] + h[i + 1:])]
                        return l
                    newB += k * n
                    ind += n
                if b == newB:
                    return [[b,0]]
                b = newB
                
        def t(b,h):
            #print(b,h)
            if (b,h) in cache:
                return cache[(b,h)]
            if not b:
                return 0
            if not h:
                return float('inf')
            cnt = float('inf')
            used = set()
            for iHand,c in enumerate(h):
                if c in used:
                    continue
                used.add(c)
                for i in range(len(b)):
                    # 剪枝
                    if b[i] != c:
                        continue
                    nb = b[:i] + c + b[i:]
                    #print(b[:i] + '[' + c + ']' + b[i:],h[:iHand] + h[iHand + 1:])
                    nbs = rebuild(nb,h[:iHand] + h[iHand + 1:])
                    for nb,ad in nbs:
                        cnt = min(cnt,1 + ad + t(nb,h[:iHand] + h[iHand + 1:]))
            cache[(b,h)] = cnt
            return cache[(b,h)]
        
        cntB = collections.Counter(board)
        cntH = collections.Counter(hand)
        for k,v in cntB.items():
            if v < 3:
                if cntB[k] + cntH[k] < 3:
                    return -1
        ans = t(board,hand)
        return -1 if ans == float('inf') else ans
        '''
        # 纯暴力
        cache = dict()
        
        def rebuild(b):
            while True:
                newB = ''
                for k,g in itertools.groupby(b):
                    n = len(list(g))
                    if n >= 3:
                        continue
                    newB += k * n
                if b == newB:
                    return b
                b = newB
                
        def t(b,h):
            #print(b,h)
            if (b,h) in cache:
                return cache[(b,h)]
            if not b:
                return 0
            if not h:
                return float('inf')
            cnt = float('inf')
            used = set()
            for iHand,c in enumerate(h):
                if c in used:
                    continue
                used.add(c)
                for i in range(len(b) + 1):
                    nb = b[:i] + c + b[i:]
                    #print(b[:i] + '[' + c + ']' + b[i:],h[:iHand] + h[iHand + 1:])
                    nb = rebuild(nb)
                    cnt = min(cnt,1 + t(nb,h[:iHand] + h[iHand + 1:]))
            cache[(b,h)] = cnt
            return cache[(b,h)]
        
        cntB = collections.Counter(board)
        cntH = collections.Counter(hand)
        for k,v in cntB.items():
            if v < 3:
                if cntB[k] + cntH[k] < 3:
                    return -1
        ans = t(board,hand)
        return -1 if ans == float('inf') else ans
        '''
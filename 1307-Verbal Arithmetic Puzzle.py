class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        d = {}
        used = set()
        notZero = set()
        for w in words:
            n = len(w)
            for i,c in enumerate(w):
                d[c] = -1
                if i == 0 and n > 1:
                    notZero.add(c)
        n = len(result)
        for i,c in enumerate(result):
            d[c] = -1
            if i == 0 and n > 1:
                notZero.add(c)
        chars = list(d.keys())
        #print(chars)
        
        # dfs
        def dfs(p,wi,s): # 表示考虑从右往左第p位,考虑words[wi],当前已求和s
            #print(p,wi,s,d,used)
            #print(p)
            if p == len(result) and wi == len(words):
                if 1 <= s <= 9:
                    if s not in used and d[result[-p]] == -1 or s in used and d[result[-p]] == s:
                        return True
                    else:
                        return False
                else:
                    return False
            elif p < len(result) and wi == len(words):
                m = s % 10
                if m not in used and d[result[-p]] == -1:
                    used.add(m)
                    d[result[-p]] = m
                    if dfs(p + 1,0,s // 10):
                        return True
                    used.remove(m)
                    d[result[-p]] = -1
                    return False
                elif m in used and d[result[-p]] == m:
                    if dfs(p + 1,0,s // 10):
                        return True
                else:
                    return False
            else:
                n = len(words[wi])
                if p > n:
                    return dfs(p,wi + 1,s)
                elif p == n:
                    c = words[wi][-p]
                    if d[c] in used:
                        if c in notZero and d[c] == 0:
                            return False
                        return dfs(p,wi + 1,s + d[c])
                    else:
                        if c in notZero:
                            st = 1
                        else:
                            st = 0
                        for i in range(st,10):
                            if i in used:
                                continue
                            d[c] = i
                            used.add(i)
                            if dfs(p,wi + 1,s + i):
                                return True
                            d[c] = -1
                            used.remove(i)
                else:
                    c = words[wi][-p]
                    if d[c] in used:
                        return dfs(p,wi + 1,s + d[c])
                    else:
                        for i in range(0,10):
                            if i in used:
                                continue
                            d[c] = i
                            used.add(i)
                            if dfs(p,wi + 1,s + i):
                                return True
                            d[c] = -1
                            used.remove(i)
                        return False

        return dfs(1,0,0)
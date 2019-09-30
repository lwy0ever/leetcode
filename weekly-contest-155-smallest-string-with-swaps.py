from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        fa = [i for i in range(n)]
        #ch = [[i] for i in range(n)]
        #ss = [[c] for c in s]
        
        def getfa(i):
            if fa[i] != i:
                fa[i] = getfa(fa[i])    #修改fa[i]，而不是每次循环获取fa[i]，可以提高速度
            return fa[i]
        
        for a,b in pairs:
            if a == b:
                continue
            ta = getfa(a)
            tb = getfa(b)
            fa[tb] = ta
            #ss[ta] += ss[tb]
            #ch[ta] += ch[tb]
            #print(ss)
            #print(ch)
        #print(fa)
        #print(ss,ch)
        fas = []
        ss = defaultdict(list)
        ch = defaultdict(list)
        for i in range(n):
            t = getfa(i)
            if t == i:
                fas.append(i)
            ss[t].append(s[i])
            ch[t].append(i)
        #print(fas)
        #print(fas[0])
        ans = [''] * n
        for i in fas:
            ss[i].sort()
            ch[i].sort()
            #print(ss[i])
            #print(ch[i])
            for j in range(len(ch[i])):
                ans[ch[i][j]] = ss[i][j]
        return ''.join(ans)

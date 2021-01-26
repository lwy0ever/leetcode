from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        fa = [i for i in range(n)]  # 存储父节点
        #ch = [[i] for i in range(n)]
        #ss = [[c] for c in s]
        
        def getfa(i):
            if fa[i] != i:
                fa[i] = getfa(fa[i])    #修改fa[i]，而不是每次循环获取fa[i]，可以提高速度
            return fa[i]
        
        # 按照父节点分组
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
        fas = []    # 所有父节点
        ss = defaultdict(list)  # ss[i]存在父节点i下的所有字符
        ch = defaultdict(list)  # ch[i]存在父节点i下的所有位置
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
            # 排序
            ss[i].sort()
            ch[i].sort()
            #print(ss[i])
            #print(ch[i])
            # 把ss依次放在ch的位置上
            for j in range(len(ch[i])):
                ans[ch[i][j]] = ss[i][j]
        return ''.join(ans)
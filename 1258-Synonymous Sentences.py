class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        ws = set()
        for s1,s2 in synonyms:
            ws.add(s1)
            ws.add(s2)
        n = len(synonyms)
        father = list(range(n))
        for i in range(n - 1):
            for j in range(i + 1,n):
                if synonyms[i][0] == synonyms[j][0] or synonyms[i][0] == synonyms[j][1] or synonyms[i][1] == synonyms[j][0] or synonyms[i][1] == synonyms[j][1]:
                    father[i] = j
                    break
        ss = [set(synonyms[i]) for i in range(n)]
        for i in range(n):
            if father[i] != i:
                for s in ss[i]:
                    ss[father[i]].add(s)
                ss[i] = set()
        #print(ss)
        #print(ws)
        #print(father)
        self.ans = []
        ts = text.split()
        l = len(ts)
        def add(tt,i):
            if i == l:
                self.ans.append(' '.join(tt))
                return
            if ts[i] in ws:
                for s in ss:
                    if ts[i] in s:
                        #print(s)
                        arr = list(s)
                        arr.sort()
                        for w in arr:
                            add(tt + [w],i + 1)
            else:
                add(tt + [ts[i]],i + 1)
        add([],0)
        return self.ans
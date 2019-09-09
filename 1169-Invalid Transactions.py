from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ts = defaultdict(list)
        ans = set()
        for t in transactions:
            sp = t.split(',')
            ts[sp[0]].append((int(sp[1]),int(sp[2]),sp[3],t))
        #print(ts)
        for k in ts:
            t = ts[k]
            t.sort(key = lambda x:x[0])
            n = len(t)
            for i in range(n - 1):
                if t[i][1] > 1000:
                    ans.add(t[i][3])
                for j in range(i + 1,n):
                    #print(t[i],t[j])
                    if t[j][0] - t[i][0] <= 60 and t[j][2] != t[i][2]:
                        #print(t[i])
                        ans.add(t[i][3])
                        ans.add(t[j][3])
            if t[n - 1][1] > 1000:
                ans.add(t[n - 1][3])
        #print(ts)
        return list(ans)
            
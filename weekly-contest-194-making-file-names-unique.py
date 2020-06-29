class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        es = dict()
        for n in names:
            if n in es:
                i = es[n] + 1
                while True:
                    t = n + '(' + str(i) + ')'
                    if t not in es:
                        es[n] = i
                        es[t] = 0
                        ans.append(t)
                        break
                    i += 1
            else:
                es[n] = 0
                ans.append(n)
            #print(n,es)
        return ans
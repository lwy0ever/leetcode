class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        # 字典树
        ans = [[] for _ in range(len(smalls))]
        d = dict()
        for i,s in enumerate(smalls):
            cur = d
            for c in s:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
            cur['#'] = i    # 由于smalls无重复,可以用#统一标识
        #print(d)
        minLen = min([len(s) for s in smalls])
        n = len(big)
        for i in range(n - minLen + 1):
            w = big[i:]
            cur = d
            for c in w:
                if c in cur:
                    cur = cur[c]
                    if '#' in cur:
                        ans[cur['#']].append(i)
                else:
                    break
            #print(w,ans)
        return ans
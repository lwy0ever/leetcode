class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        if n == 0:
            return 0
        from collections import defaultdict,Counter
        cnt = Counter(text)
        ssub = defaultdict(list)
        prec = text[0]
        st = 0
        l = 1
        for i in range(1,n):
            c = text[i]
            if c == prec:
                l += 1
            else:
                ssub[prec].append((st,l))
                prec = c
                st = i
                l = 1
        ssub[prec].append((st,l))
        ans = 0
        for k in ssub:
            ss = ssub[k]
            kn = len(ss)
            if kn == 1:
                ans = max(cnt[k],ans)
                continue
            for i in range(kn - 1):
                if ss[i][0] + ss[i][1] + 1 == ss[i + 1][0]:
                    mi = min(ss[i][1]+ss[i+1][1]+1,cnt[k])
                    ans = max(mi,ans)
                else:
                    ans = max(min(ss[i][1]+1,cnt[k]),ans)
            ans = max(min(ss[kn -1][1]+1,cnt[k]),ans)
        return ans
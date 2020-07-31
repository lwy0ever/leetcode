class Solution:
    def numSub(self, s: str) -> int:
        cnt = collections.Counter()
        n = len(s)
        ct = 1
        for i in range(1,n + 1):
            #print(ct)
            if i == n or s[i - 1] != s[i]:
                if s[i - 1] == '1':
                    cnt[ct] += 1
                ct = 0
            ct += 1
        #print(cnt)
        ans = 0
        for k,v in cnt.items():
            ans += v * (k * (k + 1) // 2) % (10 ** 9 + 7)
        return ans
                
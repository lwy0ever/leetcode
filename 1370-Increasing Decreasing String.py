class Solution:
    def sortString(self, s: str) -> str:
        cnt = collections.Counter(s)
        key = list(cnt.keys())
        key.sort()
        #print(key)
        r = 1
        ans = ''
        while cnt:
            for k in key[::r]:
                if cnt[k]:
                    ans += k
                    cnt[k] -= 1
                    if cnt[k] == 0:
                        del cnt[k]
            r = -r
            #print(cnt)
        return ans
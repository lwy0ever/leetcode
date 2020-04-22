class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        cnt = [0] * 5
        ind = {'c':0,'r':1,'o':2,'a':3,'k':4}
        for c in croakOfFrogs:
            p = ind[c]
            cnt[p] += 1
            if p == 0:
                ans = max(ans,cnt[0])
            else:
                if cnt[p] > cnt[p - 1]:
                    return -1
                if p == 4:
                    for i in range(5):
                        cnt[i] -= 1
        return ans if sum(cnt) == 0 else -1
        '''
        ans = 0
        c = 0
        r = 0
        o = 0
        a = 0
        k = 0
        for i in croakOfFrogs:
            if i == 'c':
                c += 1
                ans = max(ans,c)
            elif i == 'r':
                r += 1
                if r > c: return -1
            elif i == 'o':
                o += 1
                if o > r: return -1
            elif i == 'a':
                a += 1
                if a > o: return -1
            else:   # i == 'k'
                k += 1
                if k > a: return -1
                c -= 1
                r -= 1
                o -= 1
                a -= 1
                k -= 1
        if c == 0 and r == 0 and o == 0 and a == 0 and k == 0:
            return ans
        else:
            return -1
        '''
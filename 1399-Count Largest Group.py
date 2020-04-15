class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = collections.defaultdict(int)
        for i in range(1,n + 1):
            s = i
            t = 0
            while s > 0:
                s,m = divmod(s,10)
                t += m
            cnt[t] += 1
        _max = max(cnt.values())
        return sum(_max == v for v in cnt.values())
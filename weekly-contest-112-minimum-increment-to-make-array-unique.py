class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        ans = 0
        i = -1  # 表示cnt[k-1]已经达到的数字
        for k in sorted(cnt.keys()):
            if k > i:
                ans += (0 + cnt[k] - 1) * cnt[k] // 2
                i = k + cnt[k] - 1
            else:
                ans += ((i - k + 1) + (i - k + cnt[k])) * cnt[k] // 2
                i = i + cnt[k]
        return ans
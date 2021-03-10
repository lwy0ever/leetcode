class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = collections.Counter()
        ans = 0
        for c in s:
            cnt[c] += 1
            if cnt['L'] == cnt['R']:
                ans += 1
        return ans
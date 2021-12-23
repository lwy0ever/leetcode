class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 每次平衡就分割
        ans = 0
        cnt = 0
        for c in s:
            if c == 'L':
                cnt += 1
            else:   # c == 'R'
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans
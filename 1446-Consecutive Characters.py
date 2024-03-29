class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        pre = ''
        cnt = 0
        for c in s:
            if c == pre:
                cnt += 1
                ans = max(ans,cnt)
            else:
                pre = c
                cnt = 1
                ans = max(ans,cnt)
        return ans
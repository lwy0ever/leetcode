class Solution:
    def countLetters(self, S: str) -> int:
        ans = 0
        pre = ''
        cnt = -1
        for c in S:
            if c != pre:
                ans += (cnt + 1) * cnt // 2
                pre = c
                cnt = 1
            else:
                cnt += 1
        ans += (cnt + 1) * cnt // 2
        return ans
        
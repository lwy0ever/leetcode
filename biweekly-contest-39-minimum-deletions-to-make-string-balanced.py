class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        cntB = 0   # 记录已经出现的b的次数
        for c in s:
            if c == 'a':    # 出现了a
                if cntB > 0:   # 如果之前有b,则可以选择去掉a,或者可能可以去掉b
                    cntB -= 1
                    ans += 1
            else:
                cntB += 1
        return ans
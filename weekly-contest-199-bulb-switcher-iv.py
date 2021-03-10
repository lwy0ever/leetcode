class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        status = ['0','1']
        curStatus = 0
        for t in target:
            if t != status[curStatus]:
                ans += 1
                curStatus ^= 1
        return ans
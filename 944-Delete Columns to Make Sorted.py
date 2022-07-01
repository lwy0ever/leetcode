class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            pre = 'a'
            for c in col:
                if pre > c:
                    ans += 1
                    break
                pre = c
        return ans
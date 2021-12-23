class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s
        for i,c in enumerate(chalk):
            if k >= c:
                k -= c
            else:
                return i
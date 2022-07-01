class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in grid:
            for c in r:
                if c:
                    ans += 1
        for r in grid:
            ans += max(r)
        for c in zip(*grid):
            ans += max(c)
        return ans
class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for c in coins:
            if c & 1:
                ans += c // 2 + 1
            else:
                ans += c // 2
        return ans
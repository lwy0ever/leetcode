class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high & 1 or low & 1)
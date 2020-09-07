class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minPrice = float('inf')
        for p in prices:
            if p > minPrice:
                ans = max(ans,p - minPrice)
            minPrice = min(minPrice,p)
        return ans
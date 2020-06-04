class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        ans = []
        for c in candies:
            ans.append(c + extraCandies >= _max)
        return ans
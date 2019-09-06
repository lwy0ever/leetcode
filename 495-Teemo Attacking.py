class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        ma = 0
        for t in timeSeries:
            if t >= ma:
                ans += duration
            else:
                ans += t + duration - ma
            ma = t + duration
        return ans
                        
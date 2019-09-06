class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        ans = 0
        last = float('-inf')
        for t in intervals:
            if t[0] < last:
                ans += 1
                continue
            last = t[1]
        return ans        
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        s = [0] * n
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for i in range(n - 1):
            a = intervals[i][0]
            b = intervals[i][1]
            for j in range(i + 1,n):
                if s[j]:
                    continue
                c = intervals[j][0]
                d = intervals[j][1]
                if b >= d:
                    s[j] = 1
        return n - sum(s)
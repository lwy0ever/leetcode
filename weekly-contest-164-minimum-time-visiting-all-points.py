class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(1,n):
            ans += max(abs(points[i][0] - points[i - 1][0]),abs(points[i][1] - points[i - 1][1]))
        return ans
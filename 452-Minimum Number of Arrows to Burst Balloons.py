class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        ans = 0
        lastEnd = float('-inf')
        for start,end in points:
            if start <= lastEnd:
                continue
            else:
                ans += 1
                lastEnd = end   # 把arrow放在end的位置,可以最大可能兼顾后面的balloon
        return ans
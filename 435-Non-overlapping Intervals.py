class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照结尾位置排序,优先选中结尾位置最小的
        intervals.sort(key = lambda x:x[1])
        ans = 0
        preRight = float('-inf')
        for l,r in intervals:
            if l < preRight:
                ans += 1
            else:
                preRight = r
        return ans
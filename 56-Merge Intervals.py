class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x:x[0])
        ans = []
        t = intervals[0]
        for s,e in intervals:
            if s <= t[1]:
                t[1] = max(t[1],e)
            else:
                ans.append(t)
                t = [s,e]
        ans.append(t)
        return ans
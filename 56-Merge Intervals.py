class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x:x[0])
        ans = []
        pre = intervals[0]
        for s,e in intervals[1:]:
            if s <= pre[1]:
                pre[1] = max(pre[1],e)
            else:
                ans.append(pre)
                pre = [s,e]
        ans.append(pre)
        return ans
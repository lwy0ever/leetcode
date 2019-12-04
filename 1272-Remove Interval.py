class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        r0 = toBeRemoved[0]
        r1 = toBeRemoved[1]
        cur = 0
        while cur < len(intervals):
            if r0 <= intervals[cur][0]:
                if r1 <= intervals[cur][0]:
                    break
                elif intervals[cur][0] < r1 < intervals[cur][1]:
                    intervals[cur][0] = r1
                    break
                elif r1 >= intervals[cur][1]:
                    intervals.pop(cur)
                    continue
            elif intervals[cur][0] < r0 < intervals[cur][1]:
                if r1 < intervals[cur][1]:
                    intervals.insert(cur + 1,[r1,intervals[cur][1]])
                    intervals[cur][1] = r0
                    break
                elif r1 >= intervals[cur][1]:
                    intervals[cur][1] = r0
                    cur += 1
            else:
                cur += 1
        return intervals
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        #intervals.sort(key = lambda x:x[0])
        isOK = False
        ans = []
        for s,e in intervals:
            if isOK:
                ans.append([s,e])
                continue
            if s > newInterval[1]:
                ans.append(newInterval)
                isOK = True
                ans.append([s,e])
                continue
            if e < newInterval[0]:
                ans.append([s,e])
                continue
            newInterval = [min(newInterval[0],s),max(newInterval[1],e)]
        if not isOK:
            ans.append(newInterval)
        return ans
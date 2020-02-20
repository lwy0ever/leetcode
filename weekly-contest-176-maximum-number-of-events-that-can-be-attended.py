class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans = 0
        events.sort(reverse = True) # 倒序是为了方便pop
        minDay = events[-1][0]
        maxDay = max(x[1] for x in events)
        ends = []   # 存储结束时间
        day = minDay
        while day <= maxDay and (events or ends):
            # 把开始时间是当天的会议的结束时间放入有序队列
            while events and events[-1][0] == day:
                e = events.pop()
                bisect.insort(ends,e[1])
            # 把已经结束的会议放弃
            while ends and ends[0] < day:
                ends.pop(0)
            # 优先安排结束时间最早的会议
            if ends:
                ends.pop(0)
                ans += 1
            day += 1
        return ans
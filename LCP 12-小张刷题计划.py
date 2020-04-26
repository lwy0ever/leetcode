class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        # 注意:题目要求"按照题目编号顺序"
        # 采用二分查找法查找T
        if len(time) <= m:
            return 0
        left = 0
        right = sum(time) - max(time)
        while left < right:
            mid = (left + right) // 2
            _max,_sum,days = float('-inf'),0,1
            for t in time:
                _sum += t
                _max = max(_max,t)
                if _sum - _max > mid:   # 超过mid,不能在当天完成
                    _sum = t
                    _max = t
                    days += 1
            if days <= m:   # 提前or按时完成,缩小T
                right = mid
            else:   # 不能在m天完成,增大T
                left = mid + 1
        return left
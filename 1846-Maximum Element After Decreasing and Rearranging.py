class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # 排序后,逐个考虑可能的最大值
        arr.sort()
        m = 1
        for a in arr:
            if m == a:  # a可以作为最大值
                pass
            elif m > a: # 由于a只能减小
                m = a
            else:   # a可以减小到m
                pass
            m += 1
        return m - 1
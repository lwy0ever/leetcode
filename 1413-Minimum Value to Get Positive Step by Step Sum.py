class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min = 0
        s = 0
        for n in nums:
            s += n
            _min = min(_min,s)
        return -_min + 1 if _min < 0 else 1
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 反向考虑
        # n - 1个元素增加1
        # 等价于1个元素减1
        n = len(nums)
        m = min(nums)
        s = sum(nums)
        return s - m * n
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 最大公约数 + 裴蜀定理
        # 由「裴蜀定理」可得，题目等价于求 nums 中的全部数字的最大公约数是否等于 1
        # 若等于 1 则原数组为「好数组」，否则不是
        return functools.reduce(math.gcd,nums) == 1
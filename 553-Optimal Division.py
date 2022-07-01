class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # a / b / c
        # 通过加括号,形成 a / (b / c) = a / b * c
        # 也就是括号内第2到n个数,从除变乘,从而使数字变大
        # 括号嵌套貌似没有益处
        # 显然越多的数字从除变乘越好
        n = len(nums)
        if n == 1:
            return ''.join(map(str,nums))
        if n == 2:
            return '/'.join(map(str,nums))
        return str(nums[0]) + '/(' + '/'.join(map(str,nums[1:])) + ')'
                
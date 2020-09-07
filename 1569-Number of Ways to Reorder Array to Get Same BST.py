class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # nums[0]需要先放置
        # 令left = 小于nums[0]的数组,数量为num_left
        # right = 大于nums[0]的数组,数量为num_right
        # 那么,left和right的元素,只要保持相对顺序,left[i]和right[j]之间的顺序无所谓,可以随意穿插放置
        # 也就是说,从num_left + num_right中选择num_left个位置,依次放置left的元素,其余放置right的元素即可
        from math import comb
        def d(arr):
            # 注意,由于arr[0]位置不能动,那么len(arr) <= 2的时候,其实就没有变化了
            n = len(arr)
            if n <= 2:
                return 1
            left = [n for n in arr if n < arr[0]]
            right = [n for n in arr if n > arr[0]]
            num_left = len(left)
            num_right = len(right)
            # comb(n,k)返回从n个位置中选择k个的方案
            return comb(n - 1,num_left) * d(left) * d(right) % (10 ** 9 + 7)
        
        return (d(nums) - 1) % (10 ** 9 + 7)
        
            
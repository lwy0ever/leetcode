class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # 想象一下每个数值的贡献，正数直接给最后的总和增加价值，越大的数放后面越有利，
        # 所以先对列表降序排序，先遍历正数，然后遍历负数，遇到正数直接放到答案序列最左边
        # 而负数加入虽然会首先让总和减少，但是会让数值比它大的值往后面移动一格，又可以让总和增加
        # 所以负数的共享有两部分，如果这两部分总体加起来是正的，那负数就可以加到当前序列的最左边
        # 否则如果加入队列，会让总和减小
        # 即使是让总和保持不变，继续加下一个小于等于当前值的负值，必然会继续让总和减少，不可能产生更大的和，这时迭代停止，当前累加值就是最大和
        s = satisfaction
        s.sort(reverse = True)   # 倒序排列
        # 由于已经倒序排列
        # 每增加一个菜,将新菜加入最左侧,老菜右移,总满意度=已考虑过的菜的数值和 + 新菜满意度
        
        cur_sum = 0 # 当前已考虑过的菜的数值和
        ans = 0
        for v in s:
            if cur_sum + v <= 0:
                break
            cur_sum += v
            ans += cur_sum
        return ans
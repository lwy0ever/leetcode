class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 动态规划,优化内存
        n = len(nums)
        if n == 0:
            return 0
        up = 1    # up[i]表示包含nums[i]的情况下,最长摆动序列,并且序列最后的方向是up
        down = 1  # down[i]表示包含nums[i]的情况下,最长摆动序列,并且序列最后的方向是down
        for i in range(1,n):
            if nums[i] > nums[i - 1]:   # up
                up,down = down + 1,down
            elif nums[i] < nums[i - 1]: # down
                up,down = up,up + 1
        return max(up,down)
        '''
        # 动态规划
        n = len(nums)
        if n == 0:
            return 0
        up = [1] * n    # up[i]表示包含nums[i]的情况下,最长摆动序列,并且序列最后的方向是up
        down = [1] * n  # down[i]表示包含nums[i]的情况下,最长摆动序列,并且序列最后的方向是down
        for i in range(1,n):
            if nums[i] > nums[i - 1]:   # up
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]: # down
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:   # 平
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[-1],down[-1])
        '''
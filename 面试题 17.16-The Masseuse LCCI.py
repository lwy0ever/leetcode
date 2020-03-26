class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dpDate = [0] * n    # dpDate[i]表示在第i个时间有预约的最优方案
        dpDate[0] = nums[0]
        dpNotDate = [0] * n # dpNotDate[i]表示在第i个时间不预约的最优方案
        for i in range(1,n):
            # 上一个时间预约,本时间不预约or上一个时间不预约,本时间预约
            dpDate[i] = max(dpDate[i - 1],dpNotDate[i - 1] + nums[i])
            # 上一个时间预约,本时间不预约or上一个时间不预约,本时间也不预约
            dpNotDate[i] = max(dpDate[i - 1],dpNotDate[i - 1])
        #print(dpDate,dpNotDate)
        return max(dpDate[-1],dpNotDate[-1])
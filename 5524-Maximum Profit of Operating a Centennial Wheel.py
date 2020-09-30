class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= boardingCost * 4: # 票价不够基础成本
            return -1
        # 纯模拟
        ans = []    # ans[i]记录第i + 1轮的收入情况
        earn = 0
        queue = 0
        n = len(customers)
        i = 0
        _max = 0
        ind = -1
        while i < n or queue:
            if i < n:
                queue += customers[i]
            if queue >= 4:
                earn += boardingCost * 4 - runningCost
                queue -= 4
            else:
                earn += boardingCost * queue - runningCost
                queue = 0
            ans.append(earn)
            i += 1
            if earn > _max:
                _max = earn
                ind = i
        return ind
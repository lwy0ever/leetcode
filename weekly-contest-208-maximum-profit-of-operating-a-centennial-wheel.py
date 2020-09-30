class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= boardingCost * 4: # 票价不够基础成本
            return -1
        # 模拟
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
                # queue大于4时,最后一个整轮利润最大,直接跳到最后一个整轮
                d,queue = divmod(queue,4)
                earn += boardingCost * 4 * d - runningCost * d
                queue += sum(customers[i + 1:i + d])
                i += d - 1
            else:
                earn += boardingCost * queue - runningCost
                queue = 0
            i += 1
            if earn > _max:
                _max = earn
                ind = i
        return ind
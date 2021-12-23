class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        pre = 0
        ttl = 0
        for a,t in customers:
            if a >= pre:    # 客户到达时,厨师空闲
                ttl += t
                pre = a + t
            else:   # 厨师忙
                ttl += pre - a + t
                pre += t
        return ttl / len(customers)
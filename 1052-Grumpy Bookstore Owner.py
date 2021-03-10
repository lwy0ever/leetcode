class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # 滑动窗口
        n = len(customers)
        # 先计算不控制脾气时,满意顾客的数量
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        # 第一个窗口从0开始
        for i in range(X):
            if grumpy[i] == 1:
                ans += customers[i]
        # 滑动窗口
        right = X
        ttl = ans
        while right < n:
            if grumpy[right - X] == 1:
                ttl -= customers[right - X]
            if grumpy[right] == 1:
                ttl += customers[right]
            ans = max(ans,ttl)
            right += 1
        return ans
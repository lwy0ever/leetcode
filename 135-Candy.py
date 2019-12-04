class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n # 从左到右检查
        right = [1] * n # 从右到左检查
        for i in range(1,n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(-2,-n - 1,-1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        ans = 0
        for i in range(n):
                ans += max(left[i],right[i])
        return ans
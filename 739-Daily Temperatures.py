class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []  # 存储之前温度的下标
        n = len(T)
        ans = [0] * n
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:    # 比当前温度低的,则弹出
                ind = stack.pop()
                ans[ind] = i - ind
            stack.append(i)
        return ans
        
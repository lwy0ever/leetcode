class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 面积计算方面,参考84题(https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
        # 利用dp,计算以每个点为底,向上延伸的最大长度
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        dp = [[0] * (m + 2) for _ in range(n)]
        for i in range(m):
            if matrix[0][i] == '1':
                dp[0][i + 1] = 1
            else:
                dp[0][i + 1] = 0
        for i in range(1,n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j + 1] = dp[i - 1][j + 1] + 1
                else:
                    dp[i][j + 1] = 0
        #print(dp)
        ans = 0
        for i in range(n):
            heights = [0] + dp[i] + [0]
            # copy from problem 84
            stack = []  # 存储位置,形成一个递增序列
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    oldi = stack.pop()
                    #print(stack[-1],i,ans)
                    ans = max(ans,heights[oldi] * (i - 1 - stack[-1]))  # 位置i和位置stack[-1]不应该被包含
                stack.append(i)
                #print(stack,ans)
        return ans
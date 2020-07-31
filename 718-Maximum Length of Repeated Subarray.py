class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 子数组,需要是连续的
        nA = len(A)
        nB = len(B)
        dp = [[0] * (nB + 1) for _ in range(nA + 1)]  # dp[i][j]表示A[i:]和B[j:]的公共子数组的最大长度
        # 如果 A[i] == B[j],那么 dp[i][j] = dp[i + 1][j + 1] + 1,否则 dp[i][j] = 0
        for i in range(nA - 1,-1,-1):
            for j in range(nB - 1,-1,-1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0
        return max([max(r) for r in dp])
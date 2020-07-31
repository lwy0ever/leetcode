class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        dp = [[0] * n for _ in range(n)]    # dp[i][j]表示sum(arr[i:j + 1])
        arr = []
        for i in range(n):
            dp[i][i] = nums[i]
            arr.append(dp[i][i])
            for j in range(i + 1,n):
                dp[i][j] = dp[i][j - 1] + nums[j]
                arr.append(dp[i][j])
        #print(arr)
        arr.sort()
        #print(arr)
        return sum(arr[left - 1:right]) % (10 ** 9 + 7)
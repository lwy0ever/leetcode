class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        #dp[i][0] 表示i节点没有删除过节点的最大值
        #dp[i][1] 表示i节点删除过过节点的最大值
        
        #递归公式
        #dp[i][0] = max( arr[i], dp[i-1][0] + arr[i]) #没删除过的，是arr[i]或者 dp[i-1][0]+arr[i] 取大值
        #dp[i][1]=max(dp[i-1][0],dp[i-1][1]+arr[i]) #删除过的dp[i-1]加上本身 和 没有删除过的p[i-1]删除dp[i] 取大值
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = 0
        ans = arr[0]
        for i in range(1,n):
            dp[i][0] = max(arr[i],dp[i - 1][0] + arr[i])
            dp[i][1] = max(dp[i - 1][0],dp[i - 1][1] + arr[i])
            ans = max(ans,dp[i][0],dp[i][1])
        #print(dp)
        return ans

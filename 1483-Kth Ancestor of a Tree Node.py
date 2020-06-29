class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # dp[node][i]表示node的第2 ** i个祖先
        # 递推公式:dp[node][i] = dp[dp[node][i - 1]][i - 1]
        self.cols = int(math.log(n,2)) + 1
        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        for i in range(1,self.cols):
            for j in range(n):
                if self.dp[j][i - 1] != -1:
                    self.dp[j][i] = self.dp[self.dp[j][i - 1]][i - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.cols - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # 如果 A[i] < A[j]，我们不必考虑当 A[i] 增大时 A[j] 会减小。这是因为区间 (A[i] + K, A[j] - K) 是 (A[i] - K, A[j] + K) 的子集（这里，当 a > b 时 (a, b) 表示 (b, a) ）。
        # 这意味着对于 (up, down) 的选择一定不会差于 (down, up)。我们可以证明其中一个区间是另一个的子集，通过证明 A[i] + K 和 A[j] - K 是在 A[i] - K 和 A[j] + K 之间。
        # 对于有序的 A，设 A[i] 是最大的需要增长的 i，那么 A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K 就是计算结果的唯一值。
        n = len(A)
        A.sort()
        mi = A[0]
        ma = A[-1]
        ans = ma - mi
        for i in range(n - 1):
            a = A[i]
            b = A[i + 1]
            ans = min(ans,max(ma - K,a + K) - min(mi + K,b - K))
        return ans

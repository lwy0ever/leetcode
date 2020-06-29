class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # 得分=A[i] + A[j] + i - j
        # 也就是A[i] + i和A[j] - j
        # 对于某个点j来说,得分最大,也就意味着A[i] + i最大(i<j)
        # 用_max保存max([A[i] + i for i in range(j)])
        n = len(A)
        ans = 0
        _max = A[0] + 0
        for i in range(1,n):
            ans = max(ans,_max + A[i] - i)
            _max = max(_max,A[i] + i)
        return ans
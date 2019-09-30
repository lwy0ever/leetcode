class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A.append(-1)
        n = len(A)
        stack = []
        ans = 0
        for i in range(n):
            ind = i
            while stack and A[i] <= A[stack[-1][0]]:
                p = stack.pop()
                ind = p[1]
                ans += A[p[0]] * (i - p[0]) * (p[0] - p[1] + 1)
            stack.append((i,ind))
        #print(d)
        return ans % (10 ** 9 + 7)
            
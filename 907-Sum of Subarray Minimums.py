class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 单调栈
        arr.append(-1)
        n = len(arr)
        stack = []
        ans = 0
        for i in range(n):
            ind = i
            while stack and arr[i] <= arr[stack[-1][0]]:
                p = stack.pop()
                ind = p[1]
                ans += arr[p[0]] * (i - p[0]) * (p[0] - p[1] + 1)
            stack.append((i,ind))
        #print(d)
        return ans % (10 ** 9 + 7)
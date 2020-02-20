class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        n = len(arr)
        s = threshold * k
        t = sum(arr[:k - 1])
        for i in range(k - 1,n):
            t += arr[i]
            if t >= s:
                ans += 1
            t -= arr[i - k + 1]
        return ans
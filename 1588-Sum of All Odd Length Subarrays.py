class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for length in range(1,(n + 1) // 2 * 2,2):
            for start in range(n - length + 1):
                ans += sum(arr[start:start + length])
        return ans
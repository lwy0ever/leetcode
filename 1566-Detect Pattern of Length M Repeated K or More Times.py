class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m * k:
            return False
        for i in range(n - m * k + 1):
            for j in range(1,k):
                if arr[i:i + m] != arr[i + m * j:i + m * j + m]:
                    break
            else:
                return True
        return False
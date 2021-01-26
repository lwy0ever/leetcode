class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        return sum(arr[n // 20:n * 19 // 20]) / (n * 0.9)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        while True:
            t = numbers[l] + numbers[r]
            if t == target:
                return l + 1,r + 1
            if t < target:
                l += 1
            else:
                r -= 1
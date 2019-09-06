class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums) * len(nums[0])
        if r * c != n:
            return nums
        ans = [[0] * c for _ in range(r)]
        i = 0
        j = 0
        for num in nums:
            for e in num:
                ans[i][j] = e
                j += 1
                if j == c:
                    i += 1
                    j = 0
        return ans
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 要求i < j < k且iVal < kVal < jVal
        kVal = float("-inf")
        stack = []  # 单调递减
        for iVal in reversed(nums):
            if kVal > iVal:
                return True
            while stack and stack[-1] < iVal:   # 相当于满足了kVal < jVal
                kVal = stack.pop()  # 找到了nums[j]后面,小于jVal的最大值,记录为kVal
            stack.append(iVal)
        return False
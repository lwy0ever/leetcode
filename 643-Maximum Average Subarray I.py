class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumK = sum(nums[:k])
        ansK = sumK
        n = len(nums)
        for i in range(k,n):
            sumK = sumK + nums[i] - nums[i - k]
            ansK = max(ansK,sumK)
        return ansK / k
                
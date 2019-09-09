class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target-nums[i]] = i
        #print(d)
            
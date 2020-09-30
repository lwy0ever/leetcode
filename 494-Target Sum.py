class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        cache = dict()
        def f(ind,target):  # 当前考虑nums[ind],目标是target,返回结果数量
            if ind == n:
                if target == 0:
                    return 1
                else:
                    return 0
            if (ind,target) not in cache:
                cache[(ind,target)] = f(ind + 1,target - nums[ind]) + f(ind + 1,target + nums[ind])
            return cache[(ind,target)]
        return f(0,S)
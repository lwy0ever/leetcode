class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        _min = float('inf')
        n = len(nums)
        nums.sort()
        #print(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:    # 小优化,找到不同的值
                continue
            # 双指针
            j = i + 1
            k = n - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]: # 小优化,找到不同的值
                        k -= 1
                elif t < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: # 小优化,找到不同的值
                        j += 1
                else:
                    return target
                m = abs(t - target)
                if m < _min:
                    ans = t
                    _min = m
        return ans
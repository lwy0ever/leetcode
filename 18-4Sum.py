class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        nums.sort()
        i = 0
        while i < n-3:
            if nums[i] * 4 > target:
                break
            j = i + 1
            while j < n - 2:
                if nums[i] + nums[j] * 3 > target:
                    break
                k = j + 1
                l = n - 1
                while k < l and k < n - 1:
                    t = nums[i] + nums[j] + nums[k] + nums[l]
                    if t == target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                    elif t > target:
                        l -= 1
                    else:
                        k += 1
                j += 1
                while j <  n - 1 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
        return ans
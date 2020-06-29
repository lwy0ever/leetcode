class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 3:
            return ans
        # 排序后双指针
        nums.sort()
        #print(nums)
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                break
            j = i + 1
            l = n - 1
            while j < l:
                if nums[i] + nums[j] > 0:
                    break
                while l > j:
                    t = nums[i] + nums[j] + nums[l]
                    if t == 0:
                        ans.append([nums[i],nums[j],nums[l]])
                    elif t < 0:
                        break
                    while l > j + 1 and nums[l - 1] == nums[l]: # 避免出现重复的情况
                        l -= 1
                    l -= 1
                while j < n - 2 and nums[j] == nums[j + 1]: # 避免出现重复的情况
                    j += 1
                j += 1
            while i + 1 < n - 2 and nums[i] == nums[i + 1]: # 避免出现重复的情况
                i += 1
            i += 1
        return ans
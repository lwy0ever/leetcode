class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 当nums[i] == nums[i + 1]时
        # 如果i & 1 == 0,需要查找右侧
        # 如果i & 1 == 1,需要查找左侧
        # 所以,适用二分查找
        n = len(nums)
        if n == 1:
            return nums[0]
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            #print(l,m,r)
            if 0 < m < n - 1:   # 不是头尾
                if nums[m - 1] == nums[m]:  # 和左侧相同
                    if m & 1 == 1:  # m是奇数,查找右侧
                        l = m + 1
                    else:   # m是偶数,查找左侧
                        r = m - 2
                elif nums[m] == nums[m + 1]:  # 和右侧相同
                    if m & 1 == 1:  # m是奇数,查找左侧
                        r = m - 1
                    else:   # m是偶数,查找右侧
                        l = m + 2
                else:   # 和左右都不同
                    return nums[m]
            elif 0 == m:
                if nums[m] == nums[m + 1]:
                    l = m + 2
                else:
                    return nums[m]
            else:
                if nums[m - 1] == nums[m]:
                    r = m - 2
                else:
                    return nums[m]
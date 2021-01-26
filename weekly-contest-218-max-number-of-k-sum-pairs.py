class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 利用Counter哈希
        ans = 0
        cnt = collections.Counter(nums)
        for key,value in cnt.items():
            if k - key in cnt:
                ans += min(value,cnt[k - key])
        return ans // 2

        # 排序后,双指针,从两头检查
        ans = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                ans += 1
                l += 1
                r -= 1
        return ans
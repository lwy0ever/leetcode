class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        # 双指针
        ans = list()
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            t = nums[l] + nums[r]
            if t < target:
                l += 1
            elif t > target:
                r -= 1
            else:
                ans.append([nums[l],nums[r]])
                l += 1
                r -= 1
        return ans

        # hash
        ans = list()
        cnt = collections.Counter(nums)
        for k in sorted(cnt.keys()):
            if target - k > k:
                break
            elif target - k == k:
                ans += [[k,k]] * (cnt[k] // 2)
                break
            else:   # target - k < k
                ans += [[k,target - k]] * min(cnt[k],cnt[target - k])
            return ans

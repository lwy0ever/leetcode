class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # 方法1微调
        cnt = collections.Counter()
        ans = 0
        for n in nums:
            ans += cnt[n + k] + cnt[n - k]
            cnt[n] += 1
        return ans
        
        # 方法1:
        cnt = collections.Counter(nums)
        ans = 0
        for n in cnt.keys():
            ans += (cnt[n] * cnt[n + k]) + (cnt[n] * cnt[n - k])
        return ans // 2
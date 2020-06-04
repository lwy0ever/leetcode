class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # num_times[i]表示前缀和i出现的次数
        num_times = collections.defaultdict(int)
        num_times[0] = 1
        s = 0   # 当前的前缀和
        ans = 0
        for n in nums:
            s += n
            if s - k in num_times:
                ans += num_times[s - k]
            num_times[s] += 1
        return ans
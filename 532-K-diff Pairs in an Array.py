class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # hash
        # 空间换时间
        cnt = collections.Counter(nums)
        ans = 0
        if k == 0:
            for key in cnt.keys():
                if cnt[key] > 1:
                    ans += 1
        else:
            for key in cnt.keys():
                ans += 1 if cnt[key + k] > 0 else 0
        return ans
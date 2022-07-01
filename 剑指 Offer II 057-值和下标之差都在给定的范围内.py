class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # val和pos表示val[i]最后出现在pos[i]处
        val = []
        pos = []
        n = len(nums)
        for i in range(n):
            left = bisect.bisect_left(val,nums[i] - t)
            right = bisect.bisect_right(val,nums[i] + t)
            if right > left:
                for p in pos[left:right]:
                    if i - p <= k:
                        return True
            p = bisect.bisect(val,nums[i])
            if p and val[p - 1] == nums[i]: # nums[i]出现过
                pos[p - 1] = i
            else:
                val.insert(p,nums[i])
                pos.insert(p,i)
            #print(val)
            #print(pos)
        return False
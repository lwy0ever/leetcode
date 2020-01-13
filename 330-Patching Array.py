class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 假设 miss 是缺少的数字中最小的,则区间 [1,miss)已经被完全覆盖
        # 为了覆盖 miss,我们需要添加某些小于等于 miss 的数字,否则将不可能覆盖到
        # 假设我们添加的数字是 x,则区间 [1,miss) 和 [x,x + miss) 均被覆盖到
        # 由于 x <= miss,这两个区间必然覆盖了区间 [1,x + miss)
        # 我们希望能够尽可能选择大的 x,这样覆盖的范围就可以尽可能大
        # 因此,最好的选择是 x = miss
        ans = 0
        i = 0
        miss = 1
        l = len(nums)
        while miss <= n:
            if i < l and nums[i] <= miss:
                #print(miss,i,nums[i])
                miss += nums[i]
                i += 1
            else:
                miss += miss
                ans += 1
        return ans
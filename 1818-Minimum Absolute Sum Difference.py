class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # 排序+二分查找
        n = len(nums1)
        total = 0   # 不替换的情况下,绝对差值和
        maxReplace = float('inf')  # 记录替换后,可以减少的绝对值的最大幅度
        sorted1 = sorted(nums1)
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            if diff + maxReplace <= 0: # 可以减少的幅度已经超过了本次的diff,不需要再考虑替换nums1[i]
                continue
            ind = bisect.bisect_left(sorted1,nums2[i])    # 找nums2[i]在nums1最近的位置
            if ind > 0: # 尝试用sorted1[ind - 1]替换
                maxReplace = min(maxReplace,nums2[i] - sorted1[ind - 1] - diff)
            if ind < n: # 尝试用sorted1[ind]替换
                maxReplace = min(maxReplace,sorted1[ind] - nums2[i] - diff)
        return (total + maxReplace) % (10 ** 9 + 7) if total > 0 else total
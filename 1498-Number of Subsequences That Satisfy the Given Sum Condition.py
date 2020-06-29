class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # 非空子序列,所以只要知道该子序列的最大值和最小值,其余随意选择即可
        n = len(nums)
        i = 1
        pow2 = [2]
        bit = n
        while bit:
            pow2.append(pow2[-1] ** 2)
            bit >>= 1
        #print(pow2)
        nums.sort()
        m = 10 ** 9 + 7
        l = 0
        r = n - 1
        ans = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                # 从l + 1到r,共r - l个元素,每个元素可以选择,也可以不选择
                # ans += 2 ** (r - l)
                # 优化2 ** x的计算
                t = r - l
                #print(t)
                p = 1
                i = 0
                while t:
                    if t & 1:
                        p *= pow2[i]
                    t >>= 1
                    i += 1
                ans += p
                #print(p)
                # 优化2 ** x的计算完毕
                l += 1
            else:
                r -= 1
        return ans % m
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 考虑其中一个数字nums[i],从0达到nums[i],要经过a[i]次+1,b[i]次*2
        # 1 * 2的效率和1 + 1的效率相同
        # 其余的情况下,*2的效率必然大于+1的效率
        # 同时,b[i]可以共享操作
        # 所以*2的效率最高
        # 也就是,对于nums[i]
        # 如果是偶数,//2最好
        # 如果是奇数,先-1,然后再//2
        n = len(nums)
        a = 0
        bmax = 0
        for i in range(n):
            x = nums[i]
            b = 0
            while x > 0:
                if x & 1 == 0:
                    x >>= 1
                    b += 1
                else:
                    x ^= 1
                    a += 1
            bmax = max(bmax,b)
        return a + bmax
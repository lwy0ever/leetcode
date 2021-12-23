class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 只要找到两个点的前缀和，它们除以k的余数相同就行
        ex = defaultdict(int)   # 已经出现过的位置
        ex[0] = -1
        pre = 0
        for i,num in enumerate(nums):
            pre += num
            pre %= k
            if pre in ex: # 当前的余数 在 之前出现过,则减掉之前出现的余数,就是k的倍数了
                if i - ex[pre] >= 2:
                    return True
            else:
                ex[pre] = i
        return False
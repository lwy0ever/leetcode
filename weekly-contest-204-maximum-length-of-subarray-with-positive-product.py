class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        neg_found = 0   # 负数出现的奇数or偶数次
        neg_start = float('inf')    # 第一个负数的位置
        zero_pos = -1   # 最新的0出现的位置
        for i,n in enumerate(nums):
            if n == 0:
                # 出现了0,全部初始化
                neg_found = 0
                neg_start = float('inf')
                zero_pos = i
            elif n < 0:
                # 发现负数
                neg_found ^= 1
                neg_start = min(neg_start,i)
            
            if neg_found:   # 奇数个负数
                ans = max(ans,i - neg_start)    # 去掉第一个负数
            else:   # 偶数个负数
                ans = max(ans,i - zero_pos) # 去掉0
        return ans

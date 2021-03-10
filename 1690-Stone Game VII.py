class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # Bob尽力减小分差
        # Alice尽力扩大分差
        # 也就是,双方都尽可能获得最大的分数差
        # 考虑区间[i:j]
        # [i:j - 1]的最大分数差是A
        # [i + 1:j]的最大分数差是B
        # 则[i:j]的最大分数差就是max(sum(i:j) - value[i] - B,sum(i:j) - value[j] - A)
        n = len(stones)
        # 前缀和
        presum = [0] * (n + 1)  # 于是sum(i:j) = presum[j] - presum[i]
        for i in range(n):
            presum[i + 1] = presum[i] + stones[i]
        #print(presum)
        ans = [0] * n
        for l in range(2,n + 1):    # 考虑的区间长度
            d1 = ans[0]
            d2 = ans[1]
            for i in range(n - l + 1):
                sumIJ = presum[i + l] - presum[i]
                ans[i] = max(sumIJ - stones[i + l - 1] - ans[i],sumIJ - stones[i] - ans[i + 1])
            #print(ans)
        return ans[0]
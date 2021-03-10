class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Alice取最大的,我取次大的,Bob取最小的
        # 依次类推
        ans = 0
        piles.sort()
        n = len(piles)
        for i in range(1,n // 3 + 1):
            ans += piles[-i * 2]
        return ans
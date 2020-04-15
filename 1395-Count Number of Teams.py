class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # 左侧rate小于该士兵rate的数量 x 右侧rate大于该士兵rate的数量
        # + 左侧rate大于该士兵rate的数量 x 右侧rate小于该士兵rate的数量
        ans = 0
        n = len(rating)
        for i in range(1,n - 1):
            left = 0
            for l in range(i):
                if rating[l] < rating[i]:
                    left += 1
            right = 0
            for r in range(i + 1,n):
                if rating[r] > rating[i]:
                    right += 1
            ans += left * right + (i - left) * (n - i - 1 - right)
        return ans
        '''
        ans = 0
        n = len(rating)
        for i in range(n - 2):
            for j in range(i + 1,n - 1):
                for k in range(j + 1,n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        ans += 1
        return ans
        '''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # 方法1:计数排序
        # 时间复杂度O(N + C),C是数组heights中的最大值
        mx = max(heights)
        cnt = [0] * (mx + 1)
        for h in heights:
            cnt[h] += 1
        #print(cnt)

        ans = 0
        ind = 0
        for i in range(1,mx + 1):
            for j in range(cnt[i]):
                #print(i,j,heights[i])
                if heights[ind] != i:
                    ans += 1
                ind += 1
        return ans

        # 方法2:排序
        # 时间复杂度O(NlogN)
        expected = sorted(heights)
        return sum(a != b for a,b in zip(heights,expected))
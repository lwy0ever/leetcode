class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # 思路类似,优化优化
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx

        # 原始思路       
        n = len(nums)
        # 由于nums[i] < n
        # 对于nums[i],nums[i]的新索引在[nums[i],n)的范围内,可以使nums[i] <= 新索引
        # 可以得到使nums[i]得分的k的范围
        ranges = []
        for i,num in enumerate(nums):
            if num < i:
                # num < i时
                # k的范围
                # 0 <= k <= i
                # i < k <= i - num
                ranges.append((0,i - num))
                if i + 1 <= n - 1:
                    ranges.append((i + 1,n - 1))
            elif num == i:
                ranges.append((0,0))
                if i + 1 <= n - 1:
                    ranges.append((i + 1,n - 1))
            else:
                # num > i时
                # k的范围
                # i < k <= n - num + i
                ranges.append((i + 1,n - num + i))
            #print(i,num,ranges[-2:])
        # 前缀和
        ansRange = [0] * (n + 1)
        for s,e in ranges:
            ansRange[s] += 1
            ansRange[e + 1] -= 1
        ans = 0
        best = 0
        pre = 0
        for i in range(n + 1):
            pre += ansRange[i]
            if pre > best:
                ans = i
                best = pre
        return ans
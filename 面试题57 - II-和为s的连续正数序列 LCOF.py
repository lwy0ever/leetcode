class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 如果是连续n个数:
        # n是奇数时:
        #   中间一个数 = target // n
        #   第一个数是 target // n - (n - 1) // 2
        #   最后一个数是 target // n + (n - 1) // 2
        # n是偶数时:
        #   第一个数是 target // n - (n - 2) // 2
        #   最后一个数是 target // n + n // 2
        # .....................................
        # 序列第一个数是x,最后一个数是x + i
        # 序列和target = (x * 2 + i) * (i + 1) / 2
        # 则x = (target - i * (i + 1) // 2) / (i + 1)
        # 需要(target - i * (i + 1) // 2) % (i + 1) == 0 and target - i * (i + 1) // 2 > 0
        ans = []
        i = 1
        while i * (i + 1) // 2 < target:
            if (target - i * (i + 1) // 2) % (i + 1) == 0:
                x = target // (i + 1) - i // 2
                ans.append([x + ind for ind in range(i + 1)])
            i += 1
        return ans[::-1]
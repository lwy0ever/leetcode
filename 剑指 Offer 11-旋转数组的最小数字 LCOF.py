class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 类似二分查找
        l = 0
        r = len(numbers) - 1
        while l < r:
            # 未旋转
            if numbers[l] < numbers[r]:
                return numbers[l]
            m = (l + r) // 2
            #print(l,m,r)
            if numbers[l] < numbers[m]: # 前一半是升序
                l = m
            elif numbers[l] > numbers[m]:
                r = m
            else:   # numbers[l] == numbers[m],无法判断
                l += 1
        return numbers[l]
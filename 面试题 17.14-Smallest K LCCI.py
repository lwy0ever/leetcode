class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        # 模拟快排
        #print(arr,k)
        if k == 0:
            return []
        if len(arr) < 2:
            return arr[:k]
        mid = arr[-1]
        arr.pop()
        left = []
        right = []
        sameCnt = 1
        for a in arr:
            if a == mid:
                sameCnt += 1
            elif a < mid:
                left.append(a)
            else:
                right.append(a)
        leftLen = len(left)
        if k - sameCnt <= leftLen <= k:
            return left + [mid] * (k - leftLen)
        elif leftLen > k:
            return self.smallestK(left,k)
        else:   # leftLen < k - sameCnt
            return left + [mid] * sameCnt + self.smallestK(right,k - leftLen - sameCnt)
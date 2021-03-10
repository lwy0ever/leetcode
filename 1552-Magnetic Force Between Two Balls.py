class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        start = position[0]
        end = position[-1]
        left = min([position[i + 1] - position[i] for i in range(n - 1)])
        right = (end - start) // (m - 1)
        while left <= right:
            mid = (left + right) // 2
            #print(left,right,mid)
            pre = position[0]
            cnt = 1
            for i in range(1,n):
                if position[i] >= pre + mid:
                    cnt += 1
                    pre = position[i]
            #print(cnt)
            if cnt >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
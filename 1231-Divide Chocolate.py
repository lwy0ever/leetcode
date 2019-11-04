class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # 通过二分查找进行尝试
        K += 1
        l = 0
        r = sum(sweetness) // K
        
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            isOk = False
            cnt = 0 # 记录人数
            t = 0   # 记录当前这个人获得的巧克力数量
            for s in sweetness:
                t += s
                if t >= mid:    # 当前人已满足,尝试下一个人
                    cnt += 1
                    t = 0
                if cnt == K:    # 所有人都满足
                    ans = mid
                    l = mid + 1
                    break
            else:
                r = mid - 1
        return ans
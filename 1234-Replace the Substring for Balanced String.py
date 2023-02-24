class Solution:
    def balancedString(self, s: str) -> int:
        # 滑动窗口
        # 如果s[l:r]满足条件,则cnt(s[:l] + s[r:])中任何一个字符的长度不应该大于n // 4
        
        # 滑动策略
        # 从[l:l]开始滑动
        # 如果[l:r]是第一个满足条件的,那么[l + 1:r - x]一定不满足条件
        # 所以当左侧坐标是l + 1,右侧坐标一定大于等于r
        n = len(s)
        avg = n // 4
        cnt = collections.Counter(s)

        def check():
            for v in cnt.values():
                if v > avg:
                    return False
            return True
        
        if check():
            return 0

        r = 0
        ans = n
        for l,c in enumerate(s):
            while r < n and not check():
                cnt[s[r]] -= 1
                r += 1
            if not check():
                break
            ans = min(ans,r - l)
            cnt[c] += 1
        return ans
            

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 满足条件 -> 扩张长度1
        # 不满足条件 -> 滑动
        ans = 0
        cnt = collections.Counter()
        startPos = 0
        maxFreq = 0
        n = len(s)
        for i in range(n):
            cnt[s[i]] += 1
            maxFreq = max(maxFreq,cnt[s[i]])
            if maxFreq + k < i - startPos + 1:
                cnt[s[startPos]] -= 1
                startPos += 1
            ans = max(ans,i - startPos + 1)
        return ans
        '''
        # 双指针
        ans = 0
        cnt = collections.Counter()
        n = len(s)
        l,r = 0,0
        while r < n:
            cnt[s[r]] += 1
            r += 1
            while l <= r and cnt.most_common(1)[0][1] + k < r - l:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans,r - l)
        return ans
        '''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        r = 0
        cnt = set()
        while r < n:
            c = s[r]
            while c in cnt:
                cnt.remove(s[l])
                l += 1
            cnt.add(c)
            r += 1
            ans = max(ans,r - l)
        return ans
        '''
        n = len(s)
        # if n == 0: return 0
        ans = 0
        l = 0
        r = 0
        cnt = collections.Counter()
        while r < n:
            cnt[s[r]] += 1
            r += 1
            while cnt.most_common(1)[0][1] > 1:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans,r - l)
        return ans
        '''
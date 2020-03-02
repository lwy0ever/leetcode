class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 如果某个字符 x 在整个字符串中出现的次数 <k，那么 x 不可能出现在最终要求的子串中。因此，可以将原字符串截断为:x 左侧字符子串 + x + x 右侧字符子串
        cnt = collections.Counter(s)
        for c in set(s):
            if cnt[c] < k:
                return max(self.longestSubstring(x,k) for x in s.split(c))
        # 如果每个字符出现的次数均不小于k，则返回当前字符串的长度
        return len(s)
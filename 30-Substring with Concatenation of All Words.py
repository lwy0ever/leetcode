class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        ans = []
        if not s or not words:
            return ans
        wlen = len(words[0])
        slen = len(s)
        n = len(words)
        ws = Counter(words)
        # 滑动窗口,长度n,有wlen个起点(0到wlen - 1)
        for i in range(wlen):
            l = i   # 窗口左端
            r = i   # 窗口右端
            wnum = 0
            cnt = Counter() # 统计窗口内的word数量
            while r + wlen <= slen:
                w = s[r:r + wlen]   # 右移窗口
                r += wlen
                cnt[w] += 1 # 窗口内单词增加
                wnum += 1
                while cnt[w] > ws[w]:   # 新增加的单词是否需要
                    nw = s[l:l + wlen]  # 不需要,则左移窗口,尝试移除word,直到多余的word被移除
                    cnt[nw] -= 1
                    wnum -= 1
                    l += wlen
                if wnum == n:
                    ans.append(l)
                #print(i,cnt,l,r)
        return ans
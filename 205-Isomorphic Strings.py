class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}   # st[c]表示s中的字符c映射到t中的字符st[c]
        ts = {}   # ts[c]表示t中的字符c被s中的字符ts[c]映射
        n = len(s)
        for i in range(n):
            if s[i] not in st and t[i] not in ts:
                st[s[i]] = t[i]
                ts[t[i]] = s[i]
                continue
            if s[i] in st and t[i] in ts:
                if st[s[i]] != t[i] or ts[t[i]] != s[i]:
                    return False
            else:
                return False
        return True
        '''
        # 一行解法
        return [*map(s.index,s)] == [*map(t.index, t)]
        # 等价于 return [s.index(c) for c in s] == [t.index(c) for c in t]
        '''

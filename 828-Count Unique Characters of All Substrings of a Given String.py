class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 记录每个字符出现的位置
        # 分别考虑每个字符单独出现的子串个数
        pos = [[] for _ in range(26)]
        n = len(s)
        base = ord('A')
        for i in range(n):
            p = ord(s[i]) - base
            pos[p].append(i)
        #print(pos)
        ans = 0
        for i in range(26):
            p = [-1] + pos[i] + [n]
            for j in range(1,len(p) - 1):
                # 比如某个字符串...AXXXAXXA...,其中X表示非A的任意字符
                # 其中的子串XXXAXX,包含A的子串,可以从0,1,2,3开始,到3,4,5结束(包含结束位置)
                # 子串XXXAXX的包含A的子串数量 = (3 - (-1)) * (6 - 3) = 4 * 3
                ans += (p[j] - p[j - 1]) * (p[j + 1] - p[j])
        return ans % (10 ** 9 + 7)
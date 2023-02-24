class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 只有26个字母
        # 考虑每个字母的贡献(设字符串总长度n)
        # 某个字母在位置i
        # 上次出现的位置为a(如果之前没有出现过,则a = -1)
        # 下次出现的位置为b(如果之后没有出现过,则b = n)
        # 则这个字母在位置i的贡献度为(i - a) * (b - i)
        n = len(s)
        ans = 0
        pos = dict()
        for i,c in enumerate(s):
            if c not in pos:
                pos[c] = [-1]
            pos[c].append(i)
        for k in pos.keys():
            pos[k].append(n)
            l = len(pos[k])
            for i in range(l - 2):
                ans += (pos[k][i + 1] - pos[k][i]) * (pos[k][i + 2] - pos[k][i + 1])
        #print(pos)
        return ans

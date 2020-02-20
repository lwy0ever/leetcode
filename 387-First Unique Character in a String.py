class Solution:
    def firstUniqChar(self, s: str) -> int:
        existOnce = dict()
        existMore = set()
        for i,c in enumerate(s):
            if c in existOnce:
                del existOnce[c]
                existMore.add(c)
            elif c in existMore:
                continue
            else:   # 第一次出现
                existOnce[c] = i
        return min(existOnce.values()) if existOnce else -1
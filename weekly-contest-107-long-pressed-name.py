class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pre = ''
        n = len(typed)
        i = 0
        for c in name:
            if i < n and c != typed[i]:   # 不直接匹配,认为是连续按键
                while i < n and pre == typed[i]:
                    i += 1
            if i == n:  # typed已经用完
                return False
            if c == typed[i]:   # 匹配
                i += 1
                pre = c
            else:   # 不匹配
                return False
        while i < n and pre == typed[i]:    # 处理结尾的可能连续按键
            i += 1
        return i == n   # type是否用完
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 情况1:之前有m个0,现在有n个1
        # 如果n <= m,则+1
        # 如果n > m,则忽略
        # 情况2:之前有m个1,现在有n个0...
        pre0 = 0
        pre1 = 0
        cur0 = 0
        cur1 = 0
        ans = 0
        for c in s:
            if c == '0':
                cur0 += 1
                if cur1 > 0:    # 发生了0/1交替
                    pre1 = cur1
                    cur1 = 0
                    pre0 = 0
                if cur0 <= pre1:
                    ans += 1
            else:   # c == '1'
                cur1 += 1
                if cur0 > 0:    # 发生了0/1交替
                    pre0 = cur0
                    cur0 = 0
                    pre1 = 0
                if cur1 <= pre0:
                    ans += 1
        return ans
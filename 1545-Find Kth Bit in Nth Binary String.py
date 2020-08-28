class Solution:\u000A    def findKthBit(self, n: int, k: int) \u002D\u003E str:\u000A        # 方法1:找规律\u000A        # 对于Sn来说,Sn \u003D S(n\u002D1) + \u00271\u0027 + 反转(取反S(n \u002D 1))\u000A        # Sn的长度 \u003D len(S(n \u002D 1)) * 2 + 1 \u003D 2 ** n \u002D 1\u000A        # 对于findKthBit(n,k)\u000A        # 如果k \u003D\u003D 1,则为\u00270\u0027\u000A        # 如果k \u003D\u003D 2 ** (n \u002D 1),则findKthBit(n,k) \u003D 1\u000A        # 如果k \u003C\u003D 2 ** (n \u002D 1) \u002D 1,则findKthBit(n,k) \u003D findKthBit(n \u002D 1,k)\u000A        # 如果k \u003E 2 ** n,则findKthBit(n,k) \u003D findKthBit(n \u002D 1,2 ** n \u002D k)取反\u000A        if k \u003D\u003D 1:\u000A            return \u00270\u0027\u000A        if k \u003D\u003D 2 ** (n \u002D 1):\u000A            return \u00271\u0027\u000A        if k \u003C 2 ** (n \u002D 1):\u000A            return self.findKthBit(n \u002D 1,k)\u000A        else:\u000A            return \u00271\u0027 if self.findKthBit(n \u002D 1,2 ** n \u002D k) \u003D\u003D \u00270\u0027 else \u00270\u0027\u000A        # 方法2:无脑算法\u000A        \u0027\u0027\u0027\u000A        s \u003D \u00270\u0027\u000A        for i in range(n):\u000A            t \u003D [\u00271\u0027 if c \u003D\u003D \u00270\u0027 else \u00270\u0027 for c in s]\u000A            s +\u003D \u00271\u0027 + \u0027\u0027.join(t[::\u002D1])\u000A            if len(s) \u003E\u003D k:\u000A                return s[k \u002D 1]\u000A        \u0027\u0027\u0027
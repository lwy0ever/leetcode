class Solution:\u000A    def minInsertions(self, s: str) \u002D\u003E int:\u000A        left \u003D 0\u000A        right \u003D 0\u000A        ans \u003D 0\u000A        n \u003D len(s)\u000A        for i in range(n):\u000A            if s[i] \u003D\u003D \u0027(\u0027:\u000A                left +\u003D 1\u000A                if right \u0026 1:   # 奇数个right\u000A                    ans +\u003D 1\u000A                    right +\u003D 1  # 加一个right\u000A                while right \u003E\u003D 2 and left \u003E 0:\u000A                    left \u002D\u003D 1\u000A                    right \u002D\u003D 2\u000A                ans +\u003D right // 2   # 加right // 2个(\u000A                right \u003D 0\u000A            else:\u000A                right +\u003D 1\u000A                if left \u003D\u003D 0:\u000A                    ans +\u003D 1    # 需要1个left\u000A                    left +\u003D 1\u000A                while right \u003E\u003D 2 and left \u003E 0:\u000A                    left \u002D\u003D 1\u000A                    right \u002D\u003D 2\u000A            #print(s[i],ans,left,right)\u000A        if left \u003E 0:\u000A            if right \u003E 0:   # right \u003D\u003D 1\u000A                ans +\u003D 1\u000A                right +\u003D 1\u000A                left \u002D\u003D 1\u000A                right \u002D\u003D 2  # right变0\u000A            ans +\u003D left * 2\u000A        else:   # left \u003D\u003D 0\u000A            ans +\u003D right // 2 + (right \u0026 1) * 2\u000A        return ans
class Solution:\u000A    def findKthPositive(self, arr: List[int], k: int) \u002D\u003E int:\u000A        c \u003D 1\u000A        i \u003D 0\u000A        arr.append(float(\u0027inf\u0027))\u000A        while True:\u000A            while c !\u003D arr[i] and k \u003E 0:\u000A                c +\u003D 1\u000A                k \u002D\u003D 1\u000A            if k \u003D\u003D 0:\u000A                return c \u002D 1\u000A            c +\u003D 1\u000A            i +\u003D 1
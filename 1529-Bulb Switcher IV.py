class Solution:\u000A    def minFlips(self, target: str) \u002D\u003E int:\u000A        ans \u003D 0\u000A        status \u003D [\u00270\u0027,\u00271\u0027]\u000A        curStatus \u003D 0\u000A        for t in target:\u000A            if t !\u003D status[curStatus]:\u000A                ans +\u003D 1\u000A                curStatus ^\u003D 1\u000A        return ans
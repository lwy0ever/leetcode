class Solution:\u000A    def makeGood(self, s: str) \u002D\u003E str:\u000A        ans \u003D [\u00270\u0027]\u000A        for c in s:\u000A            if ans[\u002D1].lower() \u003D\u003D c.lower() and \u005C\u000A            (ans[\u002D1].islower() and c.isupper() \u005C\u000A             or ans[\u002D1].isupper() and c.islower()):\u000A                ans.pop()\u000A            else:\u000A                ans.append(c)\u000A        return \u0027\u0027.join(ans[1:])
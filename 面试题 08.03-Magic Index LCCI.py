class Solution:\u000A    def findMagicIndex(self, nums: List[int]) \u002D\u003E int:\u000A        for i,n in enumerate(nums):\u000A            if i \u003D\u003D n:\u000A                return i\u000A        return \u002D1
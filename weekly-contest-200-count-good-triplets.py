class Solution:\u000A    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) \u002D\u003E int:\u000A        n \u003D len(arr)\u000A        ans \u003D 0\u000A        for i in range(n):\u000A            for j in range(i + 1,n):\u000A                if abs(arr[i] \u002D arr[j]) \u003E a:\u000A                    continue\u000A                for k in range(j + 1,n):\u000A                    if abs(arr[j] \u002D arr[k]) \u003C\u003D b and abs(arr[i] \u002D arr[k]) \u003C\u003D c:\u000A                        ans +\u003D 1\u000A        return ans
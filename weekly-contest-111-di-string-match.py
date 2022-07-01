class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        l = 0
        r = n
        ans = []
        for c in s:
            if c == 'I':    # 需要升序，加入当前最小值
                ans.append(l)
                l += 1
            else:           # 需要降序，加入当前最大值
                ans.append(r)
                r -= 1
        ans.append(l)       # l == r，加入剩余的值
        return ans
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        l = 0
        r = n
        ans = []
        for c in S:
            if c == 'I':    # 需要升序，加入当前最小值
                ans.append(l)
                l += 1
            else:           # 需要降序，降入当前最大值
                ans.append(r)
                r -= 1
        ans.append(l)       # l == r，加入剩余的值
        return ans
class Solution:
    def reformatNumber(self, number: str) -> str:
        ans = []
        left = number.replace(' ','').replace('-','')
        #print(number)
        n = len(left)
        for i in range((n - 2) // 3):
            ans.append(left[i * 3:i * 3 + 3])
        tail = (n - 2) % 3 + 2
        if tail in (2,3):
            ans.append(left[-tail:])
        else:   # tail == 4
            ans += [left[-tail:-2],left[-2:]]
        return '-'.join(ans)
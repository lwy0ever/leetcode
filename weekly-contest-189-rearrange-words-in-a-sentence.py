class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = text.split()
        arr[0] = arr[0].lower()
        l = dict()  # l[x]表示长度为x的所有字符串
        for t in arr:
            x = len(t)
            if x in l:
                l[x].append(t)
            else:
                l[x] = [t]
        ans = []
        for k in sorted(l.keys()):
            ans += l[k]
        ans[0] = ans[0].title() # 等价于ans[0] = ans[0][0].upper() + ans[0][1:]
        return ' '.join(ans)
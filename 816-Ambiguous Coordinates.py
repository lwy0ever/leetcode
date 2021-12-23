class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        
        def validNum(s):
            l = len(s)
            if l == 1:
                return [s]
            rt = []
            if s[0] != '0': # 首位不是0,则可以是整数
                rt.append(s)
            else:   # 首位是0,则不能是整数,并且只能是0.xxx的形式
                if s[l - 1] == '0':
                    return rt
                else:
                    rt.append(s[0] + '.' + s[1:])
                    return rt
            if s[l - 1] == '0':
                return rt
            # 末位不是0,则可以形成小数
            for i in range(1,l):
                rt.append(s[:i] + '.' + s[i:])
            return rt

        n = len(s)
        for i in range(2,n - 1):
            a,b = s[1:i],s[i:n - 1]
            #print(f'{a},{b}')
            sa = validNum(a)
            sb = validNum(b)
            for va in sa:
                for vb in sb:
                    ans.append('(' + va + ', ' + vb + ')')
        return ans
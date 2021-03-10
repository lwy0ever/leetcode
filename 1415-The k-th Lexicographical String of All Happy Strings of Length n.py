class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # n为1时,有3个
        # n为2时,有3 * 2个
        # n为x时,有3 * (2 ** (x - 1))个
        d = ['a','b','c']
        ttl = 3 * 2 ** (n - 1)
        if k > ttl:
            return ''
        ans = []
        if k <= ttl // 3:
            ans.append('a')
        elif k <= ttl // 3 * 2:
            ans.append('b')
            k -= ttl // 3            
        else:
            ans.append('c')
            k -= ttl * 2 // 3          
        ttl //= 3
        for _ in range(n - 1):
            ttl //= 2
            if k <= ttl:
                for c in d:
                    if c != ans[-1]:
                        ans.append(c)
                        break
            else:
                for c in d[::-1]:
                    if c != ans[-1]:
                        ans.append(c)
                        break
                k -= ttl
        return ''.join(ans)
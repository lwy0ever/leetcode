class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def fib(s,l1,l2):
            a = int(s[:l1])
            b = int(s[l1:l1 + l2])
            if b >= 2 ** 31:
                return []
            ans = [a,b]
            #print(ans)
            l = l1 + l2
            while l < len(s):
                c = a + b
                l3 = len(str(c))
                if (s[l] != '0' and int(s[l:l + l3]) == c) or (s[l] == '0' and l3 == 1 and c == 0):
                    a,b = b,c
                    if c >= 2 ** 31:
                        return []
                    l += l3
                    ans.append(c)
                else:
                    return []
            if l == len(s):
                return ans
            else:
                return []
            
        n = len(S)
        i = 1   # 第一个数字的长度
        while i <= n // 2:
            j = 1   # 第二个数字的长度
            while j <= (n - i) // 2:
                ans = fib(S,i,j)
                if ans:
                    return ans
                if S[i:i + j] == '0':
                    break
                j += 1
            if S[:i] == '0':
                break
            i += 1
        return []
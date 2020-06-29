class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        m = len(pattern)
        n = len(value)
        if m == 0:
            return n == 0
        cnt = collections.Counter(pattern)
        first = pattern[0]
        firstNum = cnt[first]
        if len(cnt) == 1:
            return value[:n // cnt[first]] * m == value

        for i in range(n // firstNum + 1):
            a = value[:i]
            b = '-'
            #print([a,b])
            l = len(a)
            ind = i
            if (n - l * cnt[first]) % (m - cnt[first]) != 0:
                continue
            for p in pattern[1:]:
                if p == first:
                    #print('...',a,value[ind:ind + l])
                    if value[ind:ind + l] != a:
                        break
                    ind += l
                else:
                    if b == '-':
                        b = value[ind:ind + (n - l * cnt[first]) // (m - cnt[first])]
                        #print([a,b])
                        lb = len(b)
                        if a == b:
                            break
                        #print([a,b])
                    #print(value[ind:ind + lb],b)
                    if value[ind:ind + lb] != b:
                        break
                    ind += lb
            else:
                return True
        return False
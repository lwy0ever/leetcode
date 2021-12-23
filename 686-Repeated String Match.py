class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 寻找b[0]在a中的位置
        aLen = len(a)
        bLen = len(b)
        for i,c in enumerate(a):
            if c == b[0]:
                # a包含b
                if b == a[i:i + bLen]:
                    return 1
                # 找到b[0]在a中的位置,尝试匹配a[i:]
                if a[i:] == b[:aLen - i]:
                    #print(i)
                    for j in range(aLen - i,bLen,aLen):
                        # 还没有到b的末尾
                        if j + aLen < bLen:
                            if b[j:j + aLen] != a:
                                break
                        else:   # 到了b的末尾
                            if b[j:bLen] == a[:bLen - j]:
                                return (i + bLen) // aLen if (i + bLen) % aLen == 0 else (i + bLen) // aLen + 1
                            else:
                                break
                    else:   # 针对没有进入j循环的情况
                        return (i + bLen) // aLen if (i + bLen) % aLen == 0 else (i + bLen) // aLen + 1

        return -1
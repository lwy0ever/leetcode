class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        # 如果Aprefix + Bsuffix是回文串
        # 假设Aprefix比较长,则Aprefix = Ap1 + Ap2,其中Ap2是回文串,Ap1和Bsuffix对称
        for i in range(n // 2): # 尝试找到Ap1和Bsuffix对称的最长长度
            if a[i] != b[- i - 1]:
                break
        else:   # 如果完全对称,则返回True
            return True
        #print('a',i)
        # 判断剩余的Ap2或者Bp2是不是回文
        if a[i:n - i] == a[i:n - i][::-1] or b[i:n - i] == b[i:n - i][::-1]:
            return True
        for i in range(n // 2): # 尝试找到Bp1和Asuffix对称的最长长度
            #print(b[i],a[- i - 1])
            if b[i] != a[- i - 1]:
                break
        else:   # 如果完全对称,则返回True
            return True
        #print('b',i)
        # 判断剩余的Ap2或者Bp2是不是回文
        if a[i:n - i] == a[i:n - i][::-1] or b[i:n - i] == b[i:n - i][::-1]:
            return True
        return False
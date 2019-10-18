class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 前(n - 1)!个,第1位是1(1-n里最小的值)
        # 第(n - 1)! + 1到(n - 1)! * 2个,第1位是2(1-n里第2小的值)
        # ...
        # 在(n - 1)!个内,前(n-2)!个,第2位是除第1位数字的1-n里面,最小的值
        # 在(n - 1)!个内,前(n-2)! + 1到(n-2)! * 2个,第2位是除第1位数字的1-n里面,第2小的值
        factorial = 1   # 阶乘
        # (n - 1)!
        for i in range(1,n):
            factorial *= i
        noUsed = list(range(1,n + 1))
        k -= 1  # 由于k从1开始,因此将k-1,便于后面运算
        ans = ''
        toDiv = n - 1
        while toDiv:
            d,k = divmod(k,factorial)   # d表示首位数字的位置,新的k表示在新分组里面的位置(从0开始)
            ans += str(noUsed.pop(d))
            factorial //= toDiv
            toDiv -= 1
        ans += str(noUsed[0])
        return ans
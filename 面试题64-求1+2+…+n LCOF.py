class Solution:
    def sumNums(self, n: int) -> int:
        # 1,用递归
        # 2,利用条件判断语句的执行顺序,达到在0的时候不再递归的效果
        # 3,x and y:如果 x 为 False,返回 False;否则它返回 y 的计算值
        return n >= 1 and (n + self.sumNums(n - 1))
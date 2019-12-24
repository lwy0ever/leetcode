class Solution:
    def addDigits(self, num: int) -> int:
        # 假设num = 10 ** n * num[0] + 10 ** (n - 1) * num[1] + ... + 10 ** 0 * num[n]
        # 第一步计算,得到的是ans1 = num[0] + num[1] + ... + num[n]
        # num - ans1 = int('9' * (n - 1)) * num[0] + int('9' * (n - 2)) * num[0] + ... + 9 * num[n - 1] + 0
        # 所以ans1和num对9取余数的结果是相同的
        # 同理,ans2和ans1对9取余数的结果相同...
        # ans和num对9取余数的结果相同
        # 特别的,当num % 9 == 0的时候,ans不等于0,而是等于9,需要特别处理
        return (num - 1) % 9 + 1 if num > 0 else 0
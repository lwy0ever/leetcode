class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 给定一个数字序列 ABCDEF,如果数字A大于数字B,则应该删掉A
        # 所以在可以删除的情况下,序列应该是一个非递减序列
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
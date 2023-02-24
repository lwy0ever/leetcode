class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 从后向前
        ans = list()
        tailStack = list()  # 从尾部开始存入,单调递增
        for p in prices[::-1]:
            discount = 0
            while tailStack and p < tailStack[-1]:
                tailStack.pop()
            afterDiscount = p - tailStack[-1] if tailStack else p
            ans.append(afterDiscount)
            tailStack.append(p)
            #print(ans,tailStack)
        return ans[::-1]
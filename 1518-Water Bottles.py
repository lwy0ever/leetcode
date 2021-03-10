class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 1 * 酒(不含瓶) + 1 * 空瓶 = numExchange * 空瓶
        # 所以酒(不含瓶) = (numExchange - 1) * 空瓶
        # 由于最后一定会剩余1个或以上的空瓶,所以需要-1
        return (numBottles * numExchange - 1) // (numExchange - 1)

        # 正常计算
        '''
        ans = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            d,m = divmod(emptyBottles,numExchange)
            ans += d
            emptyBottles = d + m
        return ans
        '''
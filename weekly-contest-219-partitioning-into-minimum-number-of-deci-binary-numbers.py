class Solution:
    def minPartitions(self, n: str) -> int:
        # 优化,先取max,再int
        return int(max(n))

        # 每一位上的数字x,最少可以由x个1组成
        # 如果其它位上需要的数字多于x,则x提供若干个0
        return max(int(x) for x in n)
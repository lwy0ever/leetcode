class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # 前缀和
        preCal = list(accumulate(candiesCount))
        # 从第0天开始吃,可以吃favoriteDay + 1天
        ans = []
        for ft,fd,dc in queries:
            preLeast = fd  # 到前一天至少已经吃的糖果数量
            needMost = (fd + 1) * dc    # 到今天最多吃的糖果数量
            preTypeCount = 0 if ft == 0 else preCal[ft - 1]  # 之前类型的糖果总数
            
            ans.append(preLeast < preCal[ft] and needMost > preTypeCount)
        return ans
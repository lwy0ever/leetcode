class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # 将左右的rods分别设置为-x和+x,放弃的视为0
        # 则最终目标是0的,是可行的方案
        @lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')   # 利用float('-inf')吃掉无效的组合方式
            return max(dp(i + 1, s),    # 该方案放弃rods[i]
                       dp(i + 1, s - rods[i]),  # 该方案将rods[i]设为-x
                       dp(i + 1, s + rods[i]) + rods[i])    # 该方案将rods[i]设为+x,记录rods[i]

        return dp(0, 0)

        # 也超时
        '''
        _sum = sum(rods)
        n = len(rods)
        achieved = {0}   # achieved表示单一高度可达
        mask = collections.defaultdict(set)    # mask[i]记录达成i的可能组合
        mask[0] = {0}
        for i,r in enumerate(rods):
            newAchieved = set()
            #print(achieved)
            for a in sorted(achieved,reverse = True):
                if a + r > _sum:
                    continue
                newAchieved.add(a + r)
                for m in mask[a]:
                    mask[a + r].add((1 << i) | m)
                #print(a,a + r)
                #print(mask[a])
                #print(mask[a + r])
            achieved |= newAchieved
            #print(achieved)
            #print(mask)
        #print(mask[517],mask[503])
        for i in sorted(achieved,reverse = True):
            if i & 1:
                continue
            half = i // 2
            if half not in achieved:
                continue
            for mA in mask[i]:
                for mB in mask[half]:
                    if mA & mB == mB:
                        return half
        return 0
        '''

        '''
        # 也超时
        # 将数分成2组,有2 ** (n - 1)种方案(用n - 1而不是n,是因为1001和0110是一种方案)
        # 然后判断每组分别可以组成的高度,找到共有的最大高度
        n = len(rods)
        mask = 2 ** n - 1
        ans = 0
        for i in range(1,2 ** (n - 1)):
            left = i
            right = mask ^ i
            leftSum = 0
            rightSum = 0
            print(bin(left),bin(right))
            for j in range(n):
                if left & (1 << j):
                    leftSum += rods[j]
                else:
                    rightSum += rods[j]
            maxSum = min(leftSum,rightSum)
            #print(maxSum)
            achievedLeft = [0] * (maxSum + 1)
            achievedLeft[0] = 1
            achievedRight = [0] * (maxSum + 1)
            achievedRight[0] = 1
            for k in range(n):
                if left & (1 << k):
                    for x in range(maxSum - rods[k],-1,-1):
                        if achievedLeft[x] == 1:
                            achievedLeft[x + rods[k]] = 1
                else:
                    for x in range(maxSum - rods[k],-1,-1):
                        if achievedRight[x] == 1:
                            achievedRight[x + rods[k]] = 1
            #print(achievedLeft,achievedRight)
            for k in range(maxSum,0,-1):
                if achievedLeft[k] == achievedRight[k] and achievedLeft[k] == 1:
                    ans = max(ans,k)
                    break
            #print(ans)
        return ans
        '''
        
        '''
        # 会超时
        # 先选出使用的和放弃的支架,有2 ** n种方案
        # 然后看使用的支架是否可以平均分成2组
        n = len(rods)
        rods.sort(reverse = True)
        s = sum(rods)
        cache = set()   # 记录所有可能的选择
        self.ans = 0
        
        def maxHeight(arr: tuple):
            target = sum(arr) // 2
            achieved = [0] * (target + 1)
            achieved[0] = 1
            mh = 0
            for a in arr:
                for i in range(target):
                    if achieved[i] == 1 and i + a <= target:
                        achieved[i + a] = 1
            #print(achieved,target,arr)
            return target if achieved[-1] == 1 else 0

        def t(i: int,pre: List[int]) -> None:
            if i == n:
                if sum(pre) & 1 == 0 and len(pre) >= 2:
                    tuplePre = tuple(pre)
                    if tuplePre not in cache:
                        self.ans = max(self.ans,maxHeight(tuplePre))
                        cache.add(tuplePre)
                return
            t(i + 1,pre + [rods[i]])
            t(i + 1,pre)
        t(0,[])
        #print(cache)       
        
        return self.ans
        '''
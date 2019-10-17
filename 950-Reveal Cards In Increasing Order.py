class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 方法1
        # 将所有操作反向进行有可以了
        # 正操作:
        # 1. 从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。 (逆操作： 将牌放到牌组顶部)
        # 2. 如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。（逆操作： 如果牌组中有牌，将牌组底部的牌放在牌组的顶部）
        # 3. 如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。(逆操作： 先步骤2， 再步骤1)

        # 所以逆操作
        # 0. 将牌组倒序排序，放到手上
        # 1. 如果结果牌组中有牌，将牌组底部的牌放在牌组的顶部
        # 2. 将牌放到牌组顶部
        # 3. 如果手上还有牌，那么返回步骤 1。否则，停止行动。
        from collections import deque
        deck.sort(reverse=True)
        ans = deque()
        for i in deck:
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(i)
        return list(ans)

        # 方法2
        # 在剩余的空位中找到第二个空位放下当前最小的数
        '''
        n = len(deck)
        deck.sort()
        ans = [0] * n
        idx = 0
        i = 0
        jumped = True
        while idx < n:
            if ans[i] == 0:
                if jumped:
                    ans[i] = deck[idx]
                    idx += 1
                    jumped = False
                else:
                    jumped = True
            i += 1
            if i == n:
                i = 0
        return ans
        '''
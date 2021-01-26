class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        ans = 0
        n = len(inventory)
        inventory.sort(reverse = True)
        i = 1   # inventory的指针位置
        inventoryLeft = inventory[0]
        cnt = 1 # 与inventoryLeft同值的数量
        while orders:
            #print(orders,inventoryLeft)
            while i < n and inventoryLeft == inventory[i]:
                i += 1
                cnt += 1
            #print(inventoryLeft,cnt,i)
            if i == n:
                nxt = 0
            else:
                nxt = inventory[i]
            if cnt * (inventoryLeft - nxt) <= orders:   # 直到nxt,都不足以满足orders
                ans += cnt * (inventoryLeft + nxt + 1) * (inventoryLeft - nxt) // 2
                orders -= cnt * (inventoryLeft - nxt)
                inventoryLeft = nxt
            else:   # 可以满足orders
                d,m = divmod(orders,cnt)
                ans += cnt * (inventoryLeft + inventoryLeft - d + 1) * d // 2
                orders -= cnt * d
                inventoryLeft -= d
                ans += inventoryLeft * m
                orders = 0
            #print(orders,ans)
        return ans % (10 ** 9 + 7)
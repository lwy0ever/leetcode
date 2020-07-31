class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(pre,limit):   # 统计前缀是pre,在[1,limit]范围内的数量
            ans = 0
            cur = pre
            nxt = cur + 1
            while cur <= n:
                ans += min(nxt - 1,n) - cur + 1
                cur *= 10
                nxt *= 10
            return ans
        
        # 举例:在1-243中间找到213
        # pre=1,p指向1(pre=1是第1个数字)
        # 尝试前缀1,有1,10-19,100-199,共1 + 10 + 100个,1 + 111小于213
        # 则pre=2,p指向112(pre=2是第112个数字)
        # 尝试前缀2,有2,20-29,200-243,共1 + 10 + 44个,112 + 55小于213
        # 则pre=3,p指向167(pre=3是第167个数字)
        # 尝试前缀3,有3,30-39,共11个,167 + 11小于213
        # 则pre=4,p指向178
        # pre=5,p指向189
        # pre=6,p指向200
        # pre=7,p指向211
        # 尝试前缀7,有7,70-79,共11个,211 + 11大于213
        # 则pre=70,p指向212(pre=70是第212个数字)
        # 尝试前缀70,有70,共1个,212 + 1等于213
        # 则pre=71,p指向213,p == k,退出循环,返回pre
        pre = 1
        p = 1 # 指向当前所在位置,当counted == k时,也就是到了排位第k的数
        while p < k:
            cnt = count(pre,n)  # 当前pre前缀下所有节点的和
            if p + cnt > k:   # 在pre前缀的范围内
                p += 1
                pre *= 10
            else:   # counted + cnt <= k
                p += cnt
                pre += 1
        return pre
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # 状态压缩
        ans = 0
        n = len(word)
        status = 0    # 共10位,表示出现的次数
        # 由于一共10位,共有2 ** 10种状态,再压缩
        cnt = collections.Counter([0])
        for c in word:
            status ^= (1 << (ord(c) - ord('a')))
            # 状态A和状态B,如果满足条件,则A ^ B == 0或者 == (1 << xx)
            # A和B的状态有2 ** 10个,逐一检查B会比较慢
            # 但是1 << xx只有10种,可以反向查A ^ (1 << xx)是否是一种B状态
            ans += cnt[status]
            for i in range(10):
                ans += cnt[status ^ (1 << i)]
            cnt[status] += 1
            #print(cnt)
        #print(status)
        return ans
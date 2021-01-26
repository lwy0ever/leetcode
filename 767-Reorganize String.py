class Solution:
    def reorganizeString(self, S: str) -> str:
        # 方法1:
        # 统计字符个数(相比于方法2,统计个数以后不需要排序)
        # 考虑是否可以放置在奇数下标.(只要字母的出现次数不超过字符串的长度的一半,就可以放置在奇数下标)
        # 只有当字母的出现次数超过字符串的长度的一半时,才必须放置在偶数下标
        # 字母的出现次数超过字符串的长度的一半只可能发生在 n 是奇数的情况下,且最多只有一个字母的出现次数会超过字符串的长度的一半
        n = len(S)
        if n <= 1:
            return S
        cnt = collections.Counter(S)
        #print(l)
        if max(cnt.values()) > (n + 1) // 2:
            return ''
        ans = [''] * n
        even = 0
        odd = 1
        half = n // 2
        for c,ct in cnt.items():
            while ct > 0 and ct <= half and odd < n:
                ans[odd] = c
                ct -= 1
                odd += 2
            while ct > 0 and even < n:
                ans[even] = c
                ct -= 1
                even += 2
        return ''.join(ans)

        '''
        # 方法2:
        # 统计字符个数,按照个数倒序排序
        # 把出现次数最多的优先放置在偶数位置,然后放置在奇数位置
        n = len(S)
        if n <= 1:
            return S
        cnt = collections.Counter(S)
        l = []
        for c,ct in cnt.items():
            l.append([c,ct])
        l.sort(key = lambda x:-x[1])
        #print(l)
        if l[0][1] > (n + 1) // 2:
            return ''
        ans = [''] * n
        even = 0
        odd = 1
        for c,ct in l:
            while ct > 0 and even < n:
                ans[even] = c
                ct -= 1
                even += 2
            while ct > 0 and odd < n:
                ans[odd] = c
                ct -= 1
                odd += 2
        return ''.join(ans)
        '''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # n阶graycode等于n-1阶graycode,加 前缀1的n-1阶graycode的倒序
        # 举例:
        # 0阶:0
        # 1阶:0 1
        # 2阶:00 01 11 10,前2个是1阶graycode,后2个(11,10)的由来:0 1 --> 10 11 --> 11 10
        # 3阶:000 001 011 010 110 111 101 100,前4个是2阶graycode,后4个是2阶graycode加前缀1之后倒序
        ans = [0]
        for i in range(n):
            ans += [(1 << i) + v for v in ans[::-1]]
        return ans
        '''
        ans = [0]
        s = {0}
        while len(ans) < (1 << n):
            for i in range(n):
                t = ans[-1] ^ (1 << i)
                if t not in s:
                    ans.append(t)
                    s.add(t)
                    break
        return ans
        '''
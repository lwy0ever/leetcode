class Solution:
    def knightDialer(self, N: int) -> int:
        d = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[2,4]
            }
        # 末位数字的数量
        ans = [1] * 10
        for i in range(1,N):
            # 初始化新的末位数字的数量
            new_ans = [0] * 10
            # 逐个查看原末位数字
            for tail,num in enumerate(ans):
                # 转换为可能的新的末位数字
                for newtail in d[tail]:
                    new_ans[newtail] += num
            ans = new_ans
        return sum(ans) % (10 ** 9 + 7)
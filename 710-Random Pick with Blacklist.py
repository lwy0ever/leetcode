class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        #黑名单长度为s，我们从[0, N-s)中取随机值，这个随机值有可能在黑名单中，怎么办？
        #[0, N-s)内的元素，如果有i个在黑名单中，那么在[N-s, N)中，必定有i个元素不在黑名单中
        #对[0, N-s)中的黑名单元素和[N-s, N)中不在黑名单中的元素做映射m，必定可以一一对应，怎么对应倒是无所谓
        #从[0, N-s)中取随机值r，如果r不在黑名单中，直接返回；如果r在黑名单中，则m[r]一定不在黑名单，返回m[r]
        self.n = N - len(blacklist)
        # 小于s的黑名单元素集合
        black_lt_n = {b for b in blacklist if b < self.n}
        # 大于s的非黑名单元素集合
        white_gt_n = {*list(range(self.n,N))} - set(blacklist)
        # 映射关系
        self.m = dict(zip(black_lt_n,white_gt_n))

    def pick(self) -> int:
        r = random.randint(0,self.n - 1)
        return r if r not in self.m else self.m[r]


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
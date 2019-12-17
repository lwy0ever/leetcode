class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 定义一个排序函数
        def compare(x,y):
            # 需要大在前,小在后
            # 所以小于的时候返回1
            return 1 if x + y < y + x else -1
        s = map(str,nums)
        import functools
        ans = ''.join(sorted(s,key = functools.cmp_to_key(compare)))
        return '0' if ans[0] == '0' else ans
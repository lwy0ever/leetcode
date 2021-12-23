class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 定义一个针对字符串的排序函数
        # 然后排序,连接

        # 字符串比较函数
        def c(x,y):
            #print(x,y)
            if x + y > y + x:
                return -1
            return 1
        
        import functools
        s = map(str,nums)
        ans = ''.join(sorted(s,key = functools.cmp_to_key(c)))
        return '0' if ans[0] == '0' else ans
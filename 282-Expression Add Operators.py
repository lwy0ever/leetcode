class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # s:需要匹配的字符串
        # target:目标值
        # expression:已经计算过的表达式
        # res:已经计算过的表达式的值
        # prev:为了防止出现*优先级高于+和-的情况,存放最后一个被加上的数字(如果是减,则以负数表示)
        def ao(s,expression,res,prev):
            n = len(s)
            if n == 0 and res == target:
                ans.append(expression)
            for i in range(1,n + 1):
                # 处理首位是0的情况
                if s[0] == '0' and i > 1:
                    break
                a = int(s[:i])
                if len(expression) == 0:
                    ao(s[i:],s[:i],a,a)
                else:
                    ao(s[i:],expression + '+' + s[:i],res + a,a)
                    ao(s[i:],expression + '-' + s[:i],res - a,-a)
                    ao(s[i:],expression + '*' + s[:i],(res - prev) + prev * a,prev * a)

        ans = []
        ao(num,'',0,0)
        return ans
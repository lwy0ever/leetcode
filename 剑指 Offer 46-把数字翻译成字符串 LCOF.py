class Solution:
    def translateNum(self, num: int) -> int:
        c = dict()
        s = str(num)

        def t(s):
            if len(s) < 2:
                c[s] = 1
            else:
                # 00-09只有1种翻译方法:前1位+后面
                # 10-25有2种翻译方法:
                # 方法1:第1位+后面
                # 方法2:前2位+后面
                # 26-99只有1种翻译方法:前1位+后面
                if '10' <= s[:2] < '26':
                    c[s] = t(s[1:]) + t(s[2:])
                else:
                    c[s] = t(s[1:])
            #print(s,c[s])
            return c[s]
        
        t(s)
        #print(c)
        return c[s]
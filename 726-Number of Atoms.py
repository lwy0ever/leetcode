from collections import defaultdict
import re

class Solution:
    # 分析化学式f,位置从pos到n,正则模板pt(原子+数字)和pd(数字)
    # 返回ans和pos
    # ans是dict,表示每个原子的数量
    # pos是当前查到的最后的位置
    def cOA(self,f,pos,n,pt,pd):
        #print(f)
        #m = re.findall('((?:[(][a-zA-Z0-9()]*[)]|[A-Z][a-z]*))(\d*)',f)
        ans = defaultdict(int)
        while pos < n:
            # 如果当前位置是(,则继续向后查找
            if f[pos] == '(':
                #print(f[pos:],'(')
                ms,pos = self.cOA(f,pos + 1,n,pt,pd)
                #print(f[pos:],')d')
                # 如果后面跟着数量,则乘以数量
                m = pd.match(f,pos)
                for k in ms.keys():
                    ans[k] += ms[k] * (1 if m.group(1) == '' else int(m.group(1)))
                pos = m.span()[1]
            # 如果当前位置是),则返回一次
            elif f[pos] == ')':
                #print(f[pos:],')')
                return ans,pos + 1
            else:
                # 匹配原子+数量的模式
                #print(f[pos:],'x')
                m = pt.match(f,pos)
                ans[m.group(1)] += (1 if m.group(2) == '' else int(m.group(2)))
                pos = m.span()[1]
        return ans,pos

    def countOfAtoms(self, formula: str) -> str:
        pt = re.compile('([A-Z][a-z]*)(\d*)')
        pd = re.compile('(\d*)')
        n = len(formula)
        d,p = self.cOA(formula,0,n,pt,pd)
        res = ''
        for k in sorted(d.keys()):
            res += k + ('' if d[k] == 1 else str(d[k]))
        return res
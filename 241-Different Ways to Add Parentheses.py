class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        d = {}  # d[s]是一个数组,表示s可能的运算结果
        #print(nums)
        #print(ops)
        
        def compute(s):
            if s.isdigit():
                return [int(s)]
            if s in d:
                return d[s]
            
            ans = []
            for i,c in enumerate(s):
                if c in ('+','-','*'):
                    left = compute(s[:i])
                    right = compute(s[i + 1:])
                    for l in left:
                        for r in right:
                            if c == '+':
                                ans.append(l + r)
                            elif c == '-':
                                ans.append(l - r)
                            elif c == '*':
                                ans.append(l * r)
            d[s] = ans
            return ans
        
        return compute(input)
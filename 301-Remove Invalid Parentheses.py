class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            # 返回值:
            # -1表示)有问题,(也可能有问题
            # 0表示ok
            # 1表示(有问题
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return -1
            if cnt == 0:
                return 0
            else:
                return 1
        
        ans = {s}
        while True:
            toTry = set()
            valided = []
            for a in ans:
                cc = isValid(a)
                if cc == 0:
                    valided.append(a)
                elif not valided:
                    for i in range(len(a)):
                        if cc == 1 and a[i] == '(':
                            toTry.add(a[:i] + a[i + 1:])
                        elif cc == -1 and a[i] == ')':
                            toTry.add(a[:i] + a[i + 1:])
            if valided:
                return valided
            ans = toTry
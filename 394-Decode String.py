class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        cnt = 0
        n = len(s)
        numStart = 0
        cStart = 0
        i = 0
        for i,c in enumerate(s):
            if cnt == 0:
                if c.isdigit():
                    continue
                elif c == '[':
                    cnt += 1
                    num = int(s[numStart:i])
                    cStart = i + 1
                else:
                    ans.append(c)
                    numStart = i + 1
            else:
                if c == '[':
                    cnt += 1
                elif c == ']':
                    cnt -= 1
                    if cnt == 0:
                        numStart = i + 1
                        #print(s[cStart:i],num)
                        ans.append(self.decodeString(s[cStart:i]) * num)
        return ''.join(ans)
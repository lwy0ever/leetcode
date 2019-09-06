class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        mi = {1:0,2:10,3:100}
        seq = []
        
        def valid(ip):
            return int(ip) < 256 and int(ip) >= mi[len(ip)]
        
        def tryIP(st,num):
            for i in range(max(1,n - st - (num - 1) * 3),min(4,n - st - (num - 1) + 1)):
                if valid(s[st:st + i]):
                    seq.append(s[st:st + i])

                    if num > 1:
                        tryIP(st + i,num - 1)
                    else:
                        ans.append('.'.join(seq))
                    seq.pop()
        tryIP(0,4)
        return ans
        '''
        n = len(s)
        mi = {1:0,2:10,3:100}
        ans = []
        for a in range(max(1,n - 9),min(4,n - 3 + 1)):
            for b in range(max(1,n - a - 6),min(4,n - a - 2 + 1)):
                for c in range(max(1,n - a - b - 3),min(4,n - a - b - 1 + 1)):
                    d = n - a - b - c
                    #print(a,b,c,d)
                    #if s[0] == '0' and a > 1 or a == 3 and s[0] not in ('1','2') or s[a] == '0' and b > 1 or b == 3 and s[a] not in ('1','2') or c == 3 and s[a+b] not in ('1','2') or s[a+b] == '0' and c > 1 or d == 3 and s[a+b+c] not in ('1','2') or s[a+b+c] == '0' and d > 1:
                    if int(s[0:a]) >= mi[a] and int(s[0:a]) < 256 and int(s[a:a+b]) >= mi[b] and int(s[a:a+b]) < 256 and int(s[a+b:a+b+c]) >= mi[c] and int(s[a+b:a+b+c]) < 256 and int(s[-d:]) >= mi[d] and int(s[-d:]) < 256:
                        ans.append(s[0:a]+'.'+s[a:a+b]+'.'+s[a+b:a+b+c]+'.'+s[-d:])
        return ans
        '''
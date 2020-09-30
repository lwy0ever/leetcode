class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        # 交换行的时候,行本身都是不变的
        # 交换列的时候,列本身都是不变的
        # 针对每一行,需要交换列,形成01间隔的形式
        # 针对每一列,需要交换行,形成01间隔的形式
        n = len(board)
        # row:二进制形式的行
        row = [int(''.join(map(str,board[i])),2) for i in range(n)]
        # col:二进制形式的列
        col = [int(''.join(map(str,[board[j][i] for j in range(n)])),2) for i in range(n)]
        # 只能有2种行,2种列
        rc = collections.Counter(row)
        cc = collections.Counter(col)
        if len(rc.keys()) != 2 or len(cc.keys()) != 2:
            return -1
        rk = list(rc.keys())
        ck = list(cc.keys())
        # 并且这2种行(列)的^全1
        if rk[0] ^ rk[1] != (2 ** n - 1) or ck[0] ^ ck[1] != (2 ** n - 1):
            return -1
        # 并且其1的个数最多相差1
        if abs(bin(rk[0])[2:].count('1') - bin(rk[1])[2:].count('1')) > 1 or \
            abs(bin(ck[0])[2:].count('1') - bin(ck[1])[2:].count('1')) > 1:
            return -1
        ans = 0
        if n % 2 == 0:
            ans += min(sum([(rk[0] >> i) & 1 for i in range(0,n,2)]),sum([(rk[0] >> i) & 1 for i in range(1,n,2)]))
            ans += min(sum([(ck[0] >> i) & 1 for i in range(0,n,2)]),sum([(ck[0] >> i) & 1 for i in range(1,n,2)]))
        else:
            #print(rk[0],ck[0])
            if bin(rk[0])[2:].count('1') * 2 > n:   # 1开始
                ans += sum([(rk[0] >> i) & 1 == 0 for i in range(0,n,2)])
            else:   # 0开始
                ans += sum([(rk[0] >> i) & 1 == 1 for i in range(0,n,2)])
            if bin(ck[0])[2:].count('1') * 2 > n:   # 1开始
                ans += sum([(ck[0] >> i) & 1 == 0 for i in range(0,n,2)])
            else:   # 0开始
                ans += sum([(ck[0] >> i) & 1 == 1 for i in range(0,n,2)])
        return ans
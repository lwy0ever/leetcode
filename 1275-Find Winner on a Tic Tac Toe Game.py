class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        b = [[False] * 3 for _ in range(3)]
        role = 0
        di = ['A','B']
        
        def check(r):
            #print('\n'.join(map(str,b)))
            for i in range(3):
                cntCol = 0
                cntRow = 0
                for j in range(3):
                    if b[i][j] == r:
                        cntRow += 1
                    if b[j][i] == r:
                        cntCol += 1
                if cntCol == 3 or cntRow == 3:
                    return True
            cntD = 0
            cntD2 = 0
            for i in range(3):
                if b[i][i] == r:
                    cntD += 1
                if b[i][2 - i] == r:
                    cntD2 += 1
            if cntD == 3 or cntD2 == 3:
                return True
            return False

        for m in moves:
            #print(m)
            b[m[0]][m[1]] = di[role]
            #print('\n'.join(map(str,b)))
            if check(di[role]):
                return di[role]
            role ^= 1
        if len(moves) == 3 * 3:
            return 'Draw'
        else:
            return 'Pending'
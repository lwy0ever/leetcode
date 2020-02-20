class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n = len(seats)
        m = len(seats[0])
        di = [[-1,-1],[-1,1],[0,-1],[0,1]]
        checked = set()
        ans = 0
        #print('\n'.join([''.join(x) for x in seats]))
        
        def nex(i,j):
            j += 1
            if j == m:
                i += 1
                j = 0
            return i,j
        
        def pre(i,j):
            r = []
            nonlocal m
            # 由于i,j位置可以看到其左上角的人的试卷,因此需要检查前m + 1个座位的坐人情况
            for _ in range(m + 1):
                j -= 1
                if j == -1:
                    i -= 1
                    j = m - 1
                if i == -1:
                    break
                r.append(seats[i][j])
            return ''.join(r)

        def check(i,j,cnt):
            if i == n:
                return
            p = pre(i,j)
            if (p,i,j,cnt) in checked:
                return
            checked.add((p,i,j,cnt))
            x,y = nex(i,j)
            if seats[i][j] == '#':
                check(x,y,cnt)
            else:
                for d in di:
                    # 此位置不能坐人
                    if 0 <= i + d[0] < n and 0 <= j + d[1] < m:
                        if seats[i + d[0]][j + d[1]] == 'P':
                            check(x,y,cnt)
                            break
                else:
                    # 坐人
                    seats[i][j] = 'P'
                    nonlocal ans
                    ans = max(ans,cnt + 1)
                    #if ans > cnt:
                    #    print(i,j)
                    #    print('\n'.join([''.join(x) for x in seats]))
                    #    print(ans)
                    check(x,y,cnt + 1)
                    # 不坐人
                    seats[i][j] = '.'
                    check(x,y,cnt)
        check(0,0,0)
        return ans
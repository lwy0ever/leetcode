class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        if target == '0000':
            return 0
        visited = set()
        for d in deadends:
            visited.add(int(d))
        if 0 in visited:
            return -1
        t = int(target)
        fromP = {0}
        ans = 0
        while fromP:
            toP = set()
            for p in fromP:
                for i in [1,10,100,1000]:
                    # 说明p + i没有发生进位
                    if (p + i) // i % 10 != 0:
                        if p + i not in visited:
                            toP.add(p + i)
                            visited.add(p + i)
                    else:   # 发生了进位
                        newp = p + i - i * 10
                        if newp not in visited:
                            toP.add(newp)
                            visited.add(newp)
                    # 说明p - i没有发生借位
                    if (p - i) // i % 10 != 9:
                        if p - i not in visited:
                            toP.add(p - i)
                            visited.add(p - i)
                    else:   # 发生了借位
                        newp = p - i + i * 10
                        if newp not in visited:
                            toP.add(newp)
                            visited.add(newp)

            #print(toP)
            ans += 1
            if t in toP:
                return ans
            fromP = toP
        return -1
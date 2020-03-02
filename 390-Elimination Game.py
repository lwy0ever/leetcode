class Solution:
    def lastRemaining(self, n: int) -> int:
        start,end,interval = 1,n,2
        while start != end:
            last = start + (end - start) // interval * interval
            # 交换起始终点, interval翻倍且变符号
            # 注意新的终点一定是s+interval//2, 因为s已经被使用了
            # 新的起点可能是原来的e也可能是e-interval//2 (如果真正的end正好等于e)
            newEnd = start + interval // 2
            if last == end:
                newStart = end - interval // 2
            else:
                newStart = end
            interval = -interval * 2
            start,end = newStart,newEnd
        return start

        '''
        if n < 2:
            return n
        start = 2
        interval = 2
        direction = 1
        while True:
            #print(start,interval,direction)
            if direction > 0:
                start += (n - start) // interval * interval
            else:
                if start % interval == 0:
                    start = interval
                else:
                    start -= start // interval * interval
            #print(start)
            #while 0 < start + interval * direction <= n:
            #    start += interval * direction
            if (start - interval * direction <= 0 or start - interval * direction > n) and (start + interval * direction <= 0 or start + interval * direction > n):
                return start
            start -= interval * direction
            interval *= 2
            direction = -direction
        '''
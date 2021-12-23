class Solution:
    def clumsy(self, N: int) -> int:
        # 数学找规律
        # N * (N - 1) / (N - 2) 
        # = (N * (N - 2) + N) / (N - 2)
        # = N + 1 + 2 / (N - 2)
        # 对于 N = 4,为 N + 2
        # 对于 N >= 5,为 N + 1
        
        # 仅考虑大N
        # = N + 1 + (N - 3) - (N - 4 + 1) + (N - 7) - (N - 8 + 1) + ... 
        # 第一项N + 1会保留,中间的部分都会被抵消掉
        # 仅需要关注剩余的部分
        if N > 5:
            if N % 4 == 0:
                return N + 1
            elif N % 4 in (1,2):
                return N + 2
            elif N % 4 == 3:
                return N - 1
        if N <= 2:
            return N
        elif N == 3:
            return 6
        elif N == 4:
            return 7
        
        # 栈
        stack = []
        op = 0
        stack.append(N)
        while N > 1:
            N -= 1
            if op % 4 == 0: # *
                stack.append(stack.pop() * N)
            if op % 4 == 1: # /
                stack.append(int(stack.pop() / N))
            if op % 4 == 2: # +
                stack.append(N)
            if op % 4 == 3: # -
                stack.append(-N)
            op += 1
            #print(N,stack)
        return sum(stack)
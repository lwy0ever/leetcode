class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 状态压缩 + dfs,排除已用的数字
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger < desiredTotal:
            return False
        
        cache = dict()
        def dfs(status,options,desired):
            if (status,desired) in cache:
                return cache[(status,desired)]
            # 选择1时,i = 0,t = 1 << 0 = 1
            # 选择2时,i = 1,t = 1 << 1 = 2
            for i in range(len(options)):
                # 直接达标 or 对手无法达标
                if desired <= options[i] + 1 or not dfs(status | (1 << options[i]),options[:i] + options[i + 1:],desired - options[i] - 1):
                    cache[(status,desired)] = True
                    return True
            cache[(status,desired)] = False
            return False
        
        return dfs(0,list(range(maxChoosableInteger)),desiredTotal)
        '''
        # 状态压缩 + dfs
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger < desiredTotal:
            return False
        
        cache = dict()
        def dfs(status,desired):
            if (status,desired) in cache:
                return cache[(status,desired)]
            # 选择1时,i = 0,t = 1 << 0 = 1
            # 选择2时,i = 1,t = 1 << 1 = 2
            for i in range(maxChoosableInteger):
                t = 1 << i
                if status & t == 0: # 没有被用过
                    # 直接达标 or 对手无法达标
                    if desired <= i + 1 or not dfs(status | t,desired - i - 1):
                        cache[(status,desired)] = True
                        return True
            cache[(status,desired)] = False
            return False
        
        return dfs(0,desiredTotal)
        '''
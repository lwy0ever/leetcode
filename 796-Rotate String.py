class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 方法1:搜索子字符串
        # O(n)
        return len(s) == len(goal) and goal in s + s
        
        # 方法2:模拟
        # O(n ** 2)
        '''
        if s == goal:
            return True
        n = len(s)
        if len(goal) != n:
            return False
        return any(s[i:] + s[:i] == goal for i in range(1,n))
        '''
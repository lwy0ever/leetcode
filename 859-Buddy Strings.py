class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 两种情况
        # 1:s != goal,两者不同的字母数=2,且相同
        # 2:s == goal,两者包含某个字母的个数>=2
        if len(s) != len(goal):
            return False
        if s != goal:
            diffS = []
            diffG = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    diffS.append(s[i])
                    diffG.append(goal[i])
            return sorted(diffS) == sorted(diffG) and len(diffS) == 2
        else:
            return len(set(s)) < len(goal)
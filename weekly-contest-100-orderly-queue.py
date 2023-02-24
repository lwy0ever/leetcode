class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # 如果k > 1,相当于可以实现冒泡排序
        # 如果k == 1,需要找到最优解
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pal = []  # 存储自身就是回文串的word的位置
        rev_pos = dict()    # 存储反转字符串的位置信息
        for i,w in enumerate(words):
            rev_pos[w[::-1]] = i
            if w == w[::-1]:
                pal.append(i)
        ans = []
        for i,w in enumerate(words):
            if w:
                for j in range(len(w)):
                    left,right = w[:j],w[j:]
                    # left已经是回文,左侧加入right的反转
                    if left == left[::-1] and right in rev_pos and rev_pos[right] != i:
                        ans.append([rev_pos[right],i])
                    # right已经是回文,右侧加入left的反转
                    if right == right[::-1] and left in rev_pos and rev_pos[left] != i:
                        ans.append([i,rev_pos[left]])
            else:
                for p in pal:
                    if p != i:
                        ans.append([i,p])
        return ans
            
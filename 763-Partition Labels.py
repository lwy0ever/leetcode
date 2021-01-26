class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        endPos = [-1] * 26  # 字符的最后出现位置
        for i,c in enumerate(S):
            o = ord(c) - ord('a')
            endPos[o] = i
        ans = []
        start = 0
        end = 0
        for i,c in enumerate(S):
            o = ord(c) - ord('a')
            # 由于字符c的出现,包含字符c的字符串的最后结束位置需要到endPos[o]
            # 综合之前出现过的字符,最后结束位置需要到max(end,endPos[o])
            end = max(end,endPos[o])
            if end == i:    # 当前位置可以结束
                ans.append(end - start + 1)
                start = end + 1
        return ans
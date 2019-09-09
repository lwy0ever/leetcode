from collections import Counter
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        startPos = [n] * 26
        endPos = [-1] * 26
        for i in range(n):
            # 97  # ord('a')
            p = ord(S[i]) - 97
            if startPos[p] == n:
                startPos[p] = i
            endPos[p] = i
        ans = []
        mark = set()
        for p in sorted(startPos + endPos):
            if p == -1 or p == n:
                continue
            if S[p] in mark:
                mark.remove(S[p])
                if len(mark) == 0:
                    ans.append(p - start + 1)
            else:
                if not mark:    # mark is empty
                    start = p
                mark.add(S[p])

        return ans
            
            
            
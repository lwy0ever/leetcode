from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        if n == 0: return []
        l = len(words[0])
        wdd = Counter(words)
        ans = []
        #for w in words:
        #    wdd[w] += 1
        ns = len(s)
        for i in range(l):
            cnt = 0
            sdd = Counter()
            left = i
            right = i
            while right + l <= ns:
            #for j in range(i,ns,l):
                sw = s[right:right+l]
                #print(sw)
                sdd[sw] += 1
                cnt += 1
                while sdd[sw] > wdd[sw]:
                    lw = s[left:left+l]
                    left += l
                    sdd[lw] -= 1
                    cnt -= 1
                right += l
                #print(wdd,sdd)
                if cnt == n:
                    ans.append(left)
        return ans
class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ''
        words.sort(key = lambda x:(-len(x),x),reverse = True)
        cur = set()
        i = 0
        for w in words:
            if len(w) == i:
                pass
            elif len(w) == i + 1:
                i += 1
                if cur or i == 1:
                    pre = cur
                    cur = set()
                else:
                    break
            else:
                break
            if w[:-1] in pre or i == 1:
                cur.add(w)
                ans = w
            #print(w,pre,cur,ans)
        return ans
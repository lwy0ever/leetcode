class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # dfs优化
        # 对于abc->a*c这种变换,acc,adc,aec是等价的
        n = len(beginWord)
        wl = collections.defaultdict(list)
        for w in wordList:
            if len(w) != n:
                continue
            for i in range(n):
                wl[w[:i] + '*' + w[i + 1:]].append(w)
        ans = []
        visitedWord = {beginWord}
        visitedPattern = set()
        def dfs(arr):
            #print(arr,visitedPattern,visitedWord)
            if arr[-1] == endWord:
                nonlocal ans
                ans = arr.copy()
                return True
            for i in range(n):
                t = arr[-1][:i] + '*' + arr[-1][i + 1:]
                if t not in visitedPattern:
                    visitedPattern.add(t)
                    for w in wl[t]:
                        if w not in visitedWord:
                            visitedWord.add(w)
                            if dfs(arr + [w]):
                                return True
                    visitedPattern.remove(t)
            return False
        dfs([beginWord])
        return ans
        
        '''
        # dfs
        alphabet = [chr(ord('a') + i) for i in range(26)]
        wl = set(wordList)
        used = {beginWord}
        ans = []
        def dfs(arr):
            #print(arr)
            if arr[-1] == endWord:
                nonlocal ans
                ans = arr.copy()
                return True
            for i in range(len(arr[-1])):
                for a in alphabet:
                    nw = arr[-1][:i] + a + arr[-1][i + 1:]
                    if nw not in used and nw in wl:
                        used.add(nw)
                        if dfs(arr + [nw]):
                            return True
            return False
        dfs([beginWord])
        return ans
        '''
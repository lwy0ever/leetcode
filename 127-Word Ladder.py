class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        d = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                d[word[:i] + "*" + word[i + 1:]].append(word)
        #print(d)

        # 双向bfs
        cnt = 0
        fromBegin = {beginWord}
        fromEnd = {endWord}
        visited = set()
        while fromBegin:
            #print(fromBegin,fromEnd,cnt)
            cnt += 1
            toBegin = set()
            for f in fromBegin:
                #if f in fromEnd:
                #    return cnt
                visited.add(f)
                for i in range(n):
                    w = f[:i] + '*' + f[i + 1:]
                    for nw in d[w]:
                        if nw != f and nw not in visited:
                            if nw not in fromEnd:
                                toBegin.add(nw)
                            else:
                                return cnt + 1
            fromBegin = toBegin
            
            if len(fromBegin) > len(fromEnd):
                fromBegin,fromEnd = fromEnd,fromBegin
        return 0

        '''
        # bfs
        cnt = 0
        used = set()
        fromW = [beginWord]
        while fromW:
            cnt += 1
            toW = []
            for f in fromW:
                if f == endWord:
                    return cnt
                for i in range(n):
                    w = f[:i] + '*' + f[i + 1:]
                    for nw in d[w]:
                        if nw not in used:
                            used.add(nw)
                            toW.append(nw)
            fromW = toW
        return 0
        '''
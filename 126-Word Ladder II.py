class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
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
        
        def ansAdd(pathsB,pathsE,reverse):
            #print(pathsB,pathsE)
            nonlocal ans
            for pathB in pathsB:
                for pathE in pathsE:
                    if reverse:
                        ans.append(pathE + pathB[::-1])
                    else:
                        ans.append(pathB + pathE[::-1])

        # 双向bfs
        ans = []
        fromBegin = {beginWord:[[beginWord]]}   # fromBegin[w]表示到达单词w的多种路径
        fromEnd = {endWord:[[endWord]]}
        #reached = False
        reverse = False # 由于是双向bfs,需要判断当前bfs的方向
        visited = set()
        while fromBegin and fromEnd:
            #print(fromBegin,fromEnd)
            toBegin = collections.defaultdict(list)
            while fromBegin:
                f,paths = fromBegin.popitem()
                visited.add(f)
                for i in range(n):
                    w = f[:i] + '*' + f[i + 1:]
                    for nw in d[w]:
                        if nw != f and nw not in visited:   # 避免新word等于原word,避免A->B->A,以提高效率
                            if nw not in fromEnd:   # 如果首尾相接,则添加答案
                                for path in paths:
                                    toBegin[nw].append(path + [nw])
                            else:
                                #reached = True
                                ansAdd(paths,fromEnd[nw],reverse)
            if ans: # 由于是bfs,一旦遍历了当前的所有fromBegin,而且找到了结果,就是所有的最短的结果
                return ans
            fromBegin = toBegin
            
            if len(fromBegin) > len(fromEnd):
                fromBegin,fromEnd = fromEnd,fromBegin
                reverse = not reverse
        return []
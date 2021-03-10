class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.d
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = '#'
        #print(self.d)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur = [self.d]
        # bfs
        for c in word:
            if c != '.':
                newCur = []
                for ct in cur:
                    if c in ct:
                        newCur.append(ct[c])
                if not newCur:
                    return False
                cur = newCur
            else:
                newCur = []
                for ct in cur:
                    for k in ct.keys():
                        if k == '#':
                            continue
                        newCur.append(ct[k])
                cur = newCur
        #print(word,cur)
        for c in cur:
            if '#' in c:   # 查找的词必须是结尾
                return True
        return False
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.d
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        #print(self.d)
        t['end'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.d
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return 'end' in t
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.d
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
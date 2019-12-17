class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.cnt = 0
        self.comb = []
        for x in itertools.combinations(characters,combinationLength):
            self.cnt += 1
            self.comb.append(''.join(x))
            if self.cnt > 10000:
                break
        self.cur = 0

    def next(self) -> str:
        self.cur += 1
        return self.comb[self.cur - 1]

    def hasNext(self) -> bool:
        return self.cur < self.cnt
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
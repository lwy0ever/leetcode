class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = int(1000000 ** (1 / 3))
        self.hash = [[] for _ in range(self.length)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        p = key % self.length
        for item in self.hash[p]:
            if item[0] == key:
                item[1] = value
                return
        self.hash[p].append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        p = key % self.length
        for item in self.hash[p]:
            if item[0] == key:
                return item[1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        p = key % self.length
        l = len(self.hash[p])
        for i in range(l):
            if self.hash[p][i][0] == key:
                self.hash[p].pop(i)
                return
                        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
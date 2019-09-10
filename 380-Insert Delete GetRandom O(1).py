class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_index = {}
        self.data = []
        self.cnt = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data_index:
            return False
        else:
            self.data.append(val)
            self.data_index[val] = self.cnt
            self.cnt += 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data_index:
            self.data[self.data_index[val]] = self.data[-1] #把需要移除的数据和data的最后一个数据交换(由于需要移除的数据已经没有用处，所以不需要保留，直接覆盖掉)
            self.data_index[self.data[-1]] = self.data_index[val] #更新最后一个数据的位置=需要移除的数据位置
            self.data.pop()
            del self.data_index[val]
            self.cnt -= 1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data[random.randint(0,self.cnt - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
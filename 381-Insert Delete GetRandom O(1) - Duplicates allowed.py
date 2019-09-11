class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_index = {}
        self.data = []
        self.cnt = 0        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.data.append(val)
        self.cnt += 1
        if val in self.data_index:
            self.data_index[val].add(self.cnt - 1)
            #print('exist insert',self.data,self.data_index)
            return False
        else:
            self.data_index[val] = {self.cnt - 1}
            #print('not exist insert',self.data,self.data_index)
            return True        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.data_index:
            if val == self.data[-1]:
                self.data_index[val].remove(self.cnt - 1)
                if not self.data_index[val]:
                    del self.data_index[val]
                self.data.pop()
                self.cnt -= 1
                #print('remove -1',self.data,self.data_index)
                return True
            # val != self.data[-1]
            ind = self.data_index[val].pop()
            self.data_index[val].add(ind)
            self.data[ind] = self.data[-1] #把需要移除的数据和data的最后一个数据交换(由于需要移除的数据已经没有用处，所以不需要保留，直接覆盖掉)
            #print(self.cnt,ind,self.data_index[self.data[-1]])
            self.data_index[self.data[-1]].remove(self.cnt - 1)
            self.data_index[self.data[-1]].add(ind) #更新最后一个数据的位置=需要移除的数据位置
            self.data.pop()
            self.data_index[val].remove(ind)
            if not self.data_index[val]:
                del self.data_index[val]
            self.cnt -= 1
            #print('remove',self.data,self.data_index)
            return True
        else:
            return False        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.data[random.randint(0,self.cnt - 1)]        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
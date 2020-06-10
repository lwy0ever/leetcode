class LFUCache:
    # copy from powcai
    def __init__(self, capacity: int):
        from collections import OrderedDict, defaultdict
        self.freq = defaultdict(OrderedDict)    # 频率-keys,keys按照新旧顺序排序
        self.key_to_freq = dict()   # key-频率
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        key_freq = self.key_to_freq[key]
        res = self.freq[key_freq].pop(key)
        if key_freq == self.min_freq and not self.freq[key_freq]:
            self.min_freq += 1
        self.freq[key_freq + 1][key] = res
        self.key_to_freq[key] = key_freq + 1
        return res        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        # key 本身就在其中
        if key in self.key_to_freq:
            key_freq = self.key_to_freq[key]
            self.freq[key_freq].pop(key)
            if key_freq == self.min_freq and not self.freq[key_freq]:
                self.min_freq += 1
            self.freq[key_freq + 1][key] = value
            self.key_to_freq[key] = key_freq + 1
        else:
            # key不在, 要弹出频率使用次数少的key
            if len(self.key_to_freq) == self.capacity:
                k, v = self.freq[self.min_freq].popitem(last=False)
                self.key_to_freq.pop(k)
            self.key_to_freq[key] = 1
            self.freq[1][key] = value
            self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
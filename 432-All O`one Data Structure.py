class Node:
    def __init__(self,val):
        self.val = val  # val其实没有用,只是为了方便调试
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k = dict() # 存储key-cnt
        self.v = dict() # 存储cnt-Node
        self.head = Node(0)   # 指向尾部,tail.prev是最大值
        self.tail = Node(float('inf'))   # 指向头部,head.next是最小值
        self.head.next = self.tail
        self.tail.prev = self.head
        self.v[0] = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.k:
            oldValue = self.k[key]
            newValue = oldValue + 1
        else:
            oldValue = 0
            newValue = 1
        self.k[key] = newValue
        if newValue not in self.v:
            newNode = Node(newValue)
            newNode.keys.add(key)
            #print(self.v,oldValue)
            self.v[oldValue].next.prev,self.v[oldValue].next,newNode.prev,newNode.next = newNode,newNode,self.v[oldValue],self.v[oldValue].next
            self.v[newValue] = newNode
        else:
            self.v[newValue].keys.add(key)
        self.v[oldValue].keys.discard(key)
        if not self.v[oldValue].keys and oldValue > 0:
            self.v[oldValue].prev.next,self.v[oldValue].next.prev = self.v[oldValue].next,self.v[oldValue].prev
            del self.v[oldValue]

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.k:
            return
        oldValue = self.k[key]
        newValue = oldValue - 1
        if newValue > 0:
            self.k[key] = newValue
        else:
            del self.k[key]
        if newValue not in self.v:
            newNode = Node(newValue)
            newNode.keys.add(key)
            self.v[oldValue].prev.next,self.v[oldValue].prev,newNode.prev,newNode.next = newNode,newNode,self.v[oldValue].prev,self.v[oldValue]
            self.v[newValue] = newNode
        else:
            if newValue > 0:
                self.v[newValue].keys.add(key)
        self.v[oldValue].keys.discard(key)
        if not self.v[oldValue].keys:
            self.v[oldValue].prev.next,self.v[oldValue].next.prev = self.v[oldValue].next,self.v[oldValue].prev
            del self.v[oldValue]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.head.next != self.tail:
            t = self.tail.prev.keys.pop()
            self.tail.prev.keys.add(t)
            return t
        else:
            return ''
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.head.next != self.tail:
            t = self.head.next.keys.pop()
            self.head.next.keys.add(t)
            return t
        else:
            return ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
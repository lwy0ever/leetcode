class SnapshotArray:
    
    def __init__(self, length: int):
        #print('init')
        self.snid = 0
        self.snaps = {}
        self.snaps[self.snid] = {i:0 for i in range(length)}
        
    def set(self, index: int, val: int) -> None:
        self.snaps[self.snid][index] = val
    
    def snap(self) -> int:
        self.snid += 1
        self.snaps[self.snid] = {}
        return self.snid - 1
    
    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id,-1,-1):
            if index in self.snaps[i]:
                return self.snaps[i][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)